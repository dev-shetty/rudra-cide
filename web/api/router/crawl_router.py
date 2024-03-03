# License: GNU General Public License v3.0

import asyncio, json, subprocess
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


# async def execute_command(command):
#     completed_process = await asyncio.create_subprocess_exec(*command)
#     await completed_process.wait()
#     #completed_process = await asyncio.create_subprocess_shell()
#     #await completed_process.wait()


# async def send_data_to_websocket(websocket):
#         while True:
#             data = await _read_file()
#             await websocket.send_text(data)  
#             await asyncio.sleep(1)


@router.post("/generate_html")
async def get_html(data: CrawlModel):
    try:
        r = generate_yara_rule(data.keywords)
        file_path = Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar"
        with open(file_path, 'w') as f:
            f.write(f"{r}\n")
        v, c, e = True, True, True
        command = [
            'python', 
            './torcrawl/torcrawl.py', 
            str(v) and '-v', 
            str(c) and '-c', 
            '-u', data.url, 
            '-d', str(data.d), 
            '-p', str(data.p), 
            '-o', 'result.txt', 
            str(e) and '-e', 
        ]
        # subprocess.run(command)
        
        # p = subprocess.Popen(" ".join(command), stdout=subprocess.PIPE, shell=True)
        # (output, err) = p.communicate() 
        # p_status = p.wait()
        subprocess.call(command)
        return {'success': True, 'message': await _read_file()}
    except Exception as e:
        print(f"WebSocket error: {e}")
        

async def _read_file() -> str:
    """Reads contents of the specified file."""
    try:
        file_path = Path(Path(__file__).parent).parent / "torcrawl/res/keywords.yar"
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found")
        return "Error: File not found"
