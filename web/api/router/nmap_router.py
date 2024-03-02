
import json
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, Response

from workers.nmap import nmap_onion_scan

router = APIRouter()

@router.post("/")
async def model(req: Request, res: Response):
    try:
        req = json.loads(req.body)
        result = await nmap_onion_scan(req.url)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})
