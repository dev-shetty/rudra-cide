# License: GNU General Public License v3.0


import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config import *
import router.auth_router as auth_router
import router.crawl_router as crawl_router
import router.image_router as image_router
import router.alias_router as alias_router
import router.nmap_router as nmap_router

app = FastAPI(
    title="Rudra-CIDE",
    description="This is an application as a service to help our Rudra-CIDE application.",
    version="0.0.1",
    license_info={
        "name": "GNU GENERAL PUBLIC License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    docs_url="/tester",
    redoc_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def home():
    return JSONResponse({ "success": True })


app.include_router(auth_router.router, prefix="/api/v1/auth")
app.include_router(crawl_router.router, prefix="/api/v1/crawl")
app.include_router(image_router.router, prefix="/api/v1/image")
app.include_router(alias_router.router, prefix="/api/v1/alias")
app.include_router(nmap_router.router, prefix="/api/v1/nmap")


if __name__ == "__main__":
    try:
        print('------------------- Initalizing Web Server -------------------')
        print('----------------------- Service Started -----------------------')
        uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')