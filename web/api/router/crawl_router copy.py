# License: GNU General Public License v3.0

import asyncio, json
from fastapi import APIRouter, WebSocket
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
    strings_section = "\n".join([f"\t${keyword[i]} = \"{keyword}\" ascii nocase" for i, keyword in enumerate(keywords)])
    return rule_template % strings_section



async def execute_command(command):
    completed_process = await asyncio.create_subprocess_exec(*command)
    await completed_process.wait()
    #completed_process = await asyncio.create_subprocess_shell()
    #await completed_process.wait()

async def send_data_to_websocket(websocket):
        while True:
            data = await _read_file()
            await websocket.send_text(data)  
            await asyncio.sleep(1)

@router.websocket("/generate_html")
async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
    # try:
        dataRaw = await websocket.receive_text()
        data: CrawlModel = json.loads(dataRaw)
        r = generate_yara_rule(data['keywords'])
        file_path = Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar"
        with open(file_path, 'w') as f:
            f.write(f"{r}\n")
        v, c, d, p, e = True, True, 1, 1, True
        command = [
            'python', 
            'torcrawl.py', 
            str(v) and '-v', 
            str(c) and '-c', 
            '-u', data['url'], 
            '-d', str(d), 
            '-p', str(p), 
            '-o', 'result.txt', 
            str(e) and '-e', 
        ]
        subprocess_task = asyncio.create_task(execute_command(command))
        import time
        time.sleep(20)
        file_reading_task = asyncio.create_task(send_data_to_websocket(websocket))
        await asyncio.gather(subprocess_task, file_reading_task)
    # except Exception as e:
    #     print(f"WebSocket error: {e}")
    # finally:
        await websocket.close()

async def _read_file() -> str:
    """Reads contents of the specified file."""
    try:
        async with open(Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar", "r") as file:
            return await file.read()
    except FileNotFoundError:
        print(f"File not found")
        return "Error: File not found"
