# License: GNU General Public License v3.0

import requests
from fastapi import APIRouter, Request, UploadFile, File, Depends
from fastapi.responses import JSONResponse, Response

from workers.auth import verify_token

router = APIRouter()

@router.post("/")
async def model(req: Request, res: Response, token: str = Depends(verify_token)):
    try:
        data = req.body.json()
        print(data)
        return JSONResponse({ "success": True })
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})
