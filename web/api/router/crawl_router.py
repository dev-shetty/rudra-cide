# License: GNU General Public License v3.0

import time, asyncio, os
from fastapi import APIRouter, Request, UploadFile, File, WebSocket
from fastapi.responses import StreamingResponse
import subprocess
from workers.model import CrawlModel
from pathlib import Path


router = APIRouter()

def generate_yara_rule(keywords):
    rule_template = """
    rule detect_keywords
    {
        strings:
            %s
        condition:
            any of them
    }
    """
    strings_section = "\n".join([f"\t${{keyword{i}}} = \"{keyword}\" ascii nocase" for i, keyword in enumerate(keywords)])
    return rule_template % strings_section


def read_file():
    while True:
        with open(f"../torcrawl/{data.url.split('/')[-1]}/result.txt", "r") as file:
            data = file.read()
            yield data
        time.sleep(1)

@router.post('/generate_html')
async def generate_html(request: Request, data: CrawlModel):
    try:
        if not data or not data.url or not data.keywords:
            return {'status': 'failed', 'message': 'Invalid input data', }
        r = generate_yara_rule(data.keywords)
        file_path = Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar"
        with open(file_path, 'a') as f:
            f.write(f"{r}\n")
        v, c, d, p, e = True, True, 1, 1, True
        print(data.url)
        command = [
            'python', 
            'torcrawl.py', 
            v and '-v', 
            c and '-c', 
            '-u', data.url, 
            '-d', d, 
            '-p', p, 
            '-o', 'result.txt', 
            e and '-e', 
        ]
        asyncio.create_task(subprocess.run(command))
        return StreamingResponse(read_file(), media_type="text/plain")

    except Exception as err:
        print(err)
    # finally:
    #     await websocket.close()


@router.websocket("/generate_html")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        dataRaw = websocket.receive_text()
        data: CrawlModel = CrawlModel.parse_raw(dataRaw)
        r = generate_yara_rule(data.keywords)
        file_path = Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar"
        with open(file_path, 'a') as f:
            f.write(f"{r}\n")
        v, c, d, p, e = True, True, 1, 1, True
        command = [
            'python', 
            'torcrawl.py', 
            v and '-v', 
            c and '-c', 
            '-u', data.url, 
            '-d', d, 
            '-p', p, 
            '-o', 'result.txt', 
            e and '-e', 
        ]
        asyncio.create_task(subprocess.run(command))
        while True:
            data = await _read_file()
            await websocket.send_text(data)  
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

async def _read_file() -> str:
    """Reads contents of the specified file."""
    try:
        async with open(Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar", "r") as file:
            return await file.read()
    except FileNotFoundError:
        print(f"File not found")
        return "Error: File not found"
