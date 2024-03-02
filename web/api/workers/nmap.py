

import subprocess

async def nmap_onion_scan(onion_url):
    nmap_cmd = f'proxychains nmap -p 80,443 {onion_url}'
    try:
        result = subprocess.check_output(nmap_cmd, shell=True, text=True, stderr=subprocess.STDOUT)
        return {'success': True, 'result': result}
    except subprocess.CalledProcessError as e:
        print(f'Error: {e.output}')
        return { 'success': False }

# if _name_ == '_main_':
#     target_onion = 'example.onion'
#     nmap_onion_scan(target_onion)