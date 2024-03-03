# License: GNU General Public License v3.0

import requests, json, os
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from workers.exif import Exif
from workers.model import ImageExifModel, ImageModel

router = APIRouter()

@router.post("/list-image-exif")
async def list_image_exif(request: Request, data: ImageModel):
    try:
        metadata = []
        img = data.img
        img_output = './output/image/'
        exif = Exif()
        try:
            os.makedirs(img_output, exist_ok=True)
        except Exception:
            pass
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        for url in img:
            response = requests.get(url) #proxies=proxies)
            if response.status_code == 200:
                file_name = os.path.join(f"{img_output}/{url.split('/')[-1]}", os.path.basename(url))
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                    data = exif.extract_metadata(file_name)
                    if not data.get('success'):
                        metadata.append(data.get('metadata'))
                    else:
                        print(f"{url}, Failed")
                    try:
                        file.close()
                    except Exception:
                        pass
                try:
                    os.remove(file_name)
                except Exception:
                    pass
            else:
                print(f"{url}, Failed")
        return JSONResponse({ "success": True })
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})


@router.post("/image-exif")
async def image_exif(request: Request, img: ImageExifModel):
    try:
        metadata = {}
        img_output = './output/image/'
        exif = Exif()
        url = img.img
        try:
            os.makedirs(img_output, exist_ok=True)
        except Exception:
            pass
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.join(f"{img_output}/{url.split('/')[-1]}")
            with open(file_name, 'wb') as file:
                file.write(response.content)
                data = await exif.extract_metadata(file_name)
                if data['success']:
                    for key, value in data['metadata'].items():
                        metadata[f"{key}"] = f"{value}"
                else:
                    print(f"{url}, Failed")
                try:
                    file.close()
                except Exception:
                    pass
            try:
                os.remove(file_name)
            except Exception:
                pass
        else:
            print(f"{url}, Failed")
        return JSONResponse({ "success": True, 'metadata': metadata })
    except Exception as e:
        return JSONResponse({ "success": False, "message": f"Error: {e}"})
