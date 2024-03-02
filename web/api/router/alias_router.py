# License: GNU General Public License v3.0

import requests, json
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse

from workers.alias import Alias
from workers.model import AliasModel

router = APIRouter()

@router.post("/alias-user")
async def alias_user(request: Request, data: AliasModel):
    try:
        alias = Alias()
        output = await alias.check_reddit_data(data.user, data.key)
        return JSONResponse(output)
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})


# @router.post("/alias-user-guess")
# async def alias_user_guess(request: Request):
#     try:
#         data = json.loads(request.body)
#         print(data)
#         return JSONResponse({ "success": True })
#     except Exception as e:
#         return JSONResponse({ "success": False, "message": f"Error: {e}"})
