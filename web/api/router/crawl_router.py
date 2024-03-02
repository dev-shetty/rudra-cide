# License: GNU General Public License v3.0

import requests
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse
import subprocess

router = APIRouter()

@router.post('/generate_html')
async def run_python_file(url, v, c, d, p, e):
    try:
        # data = json.loads(request.body)
        print(url)
        command = [
            'python', 
            'torcrawl.py', 
            f'{v and '-v'}', 
            '-c', 
            '-u', 'http://biblemeowimkh3utujmhm6oh2oeb3ubjw2lpgeq3lahrfr2l6ev6zgyd.onion', 
            '-d', '2', 
            '-p', '1', 
            '-o', 'result.txt', 
            '-e', 
        ]
        subprocess.run(command)
        
        # print(output.stdout)
        return {'status': 'success', 'message': 'Python file executed successfully', 'output': output.stdout}
    except Exception as e:
        print(e)
        # raise HTTPException(status_code=500, detail={'status': 'error', 'message': str(e)})
