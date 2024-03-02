# License: GNU General Public License v3.0

import jwt
from fastapi import Request
from fastapi.responses import Response, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from config import KEY
from workers.crypt import decrypt, encrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_token(req: Request, res: Response, next):
    token = req.headers.get('Authorization', '').split(' ')[1]
    if not token:
        return JSONResponse(status_code=401, content={ 'success': False, 'message': 'No token provided' })
    try:
        decoded = jwt.decode(token, KEY, algorithms=["HS256"])
        req.body['id'] = await decrypt(decoded['id'])
        return next()
    except jwt.ExpiredSignatureError:
        return JSONResponse(status_code=401, content={ 'success': False, 'message': 'Token has expired' })
    except jwt.InvalidTokenError:
        return JSONResponse(status_code=401, content={ 'success': False, 'message': 'Invalid token' })
    except Exception as e:
        return JSONResponse(status_code=500, content={ 'success': False, 'message': 'Internal server error' })

async def create_token(id: str):
    try:
        token = jwt.encode({'id': await encrypt(id)}, KEY, algorithm="HS256")
        return {'success': True, 'token': token}
    except Exception as e:
        print(f"create_token: {e}")
        return JSONResponse(status_code=401, content={'success': False, 'message': 'Authentication failed'})

