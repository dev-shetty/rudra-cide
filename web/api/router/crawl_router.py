# License: GNU General Public License v3.0

import requests
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import JSONResponse
import subprocess

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


@router.post('/generate_html')
async def run_python_file(url, v, c, d, p, e, keywords):
    try:
        generate_yara_rule(keywords)
        
        # data = json.loads(request.body)
        print(url)
        command = [
            'python', 
            'torcrawl.py', 
            v and '-v', 
            c and '-c', 
            '-u', 'http://biblemeowimkh3utujmhm6oh2oeb3ubjw2lpgeq3lahrfr2l6ev6zgyd.onion', 
            '-d', d, 
            '-p', p, 
            '-o', 'result.txt', 
            e and '-e', 
        ]
        subprocess.run(command)
        
        # print(output.stdout)
        return {'status': 'success', 'message': 'Python file executed successfully', }
    except Exception as err:
        print(err)
        # raise HTTPException(status_code=500, detail={'status': 'error', 'message': str(e)})
