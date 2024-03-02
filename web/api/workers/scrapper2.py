from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from bs4 import BeautifulSoup
import time
import os

onion_url = 'http://biblemeowimkh3utujmhm6oh2oeb3ubjw2lpgeq3lahrfr2l6ev6zgyd.onion/'

options = Options()
options.headless = False  # Run WebDriver in headless mode
options.binary_location = "C:\\Tor Browser\\Browser\\firefox.exe"
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1') #defaults fault SOCKS port

def download_html(url):
    try:
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        
        # Wait until an element is present on the page (adjust timeout as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body"))
        )
        
        # Get the HTML content of the page
        html = driver.page_source
        
        # Save the HTML content to a file
        shorten=onion_url.split('//')[1].split('.')[0]
        shorten=f"scrap/{shorten}.html"
        with open(shorten, "w", encoding="utf-8") as file:
            file.write(html)
            soup = BeautifulSoup(html, 'html.parser')
            image_tag = soup.find('img')
            image_link = image_tag.get('src')
            print(image_link)
            # Download the image
            driver.get(onion_url + image_link)


            


    except TimeoutException as te:
        print("Timed out waiting for the page to load.")
    except WebDriverException as e:
        print("An error occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        driver.quit()  # Quit the WebDriver





def break_html(html_file_path, output_dir, max_size=2000):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    basename = os.path.basename(html_file_path)
    filename, ext = os.path.splitext(basename)
    output_files = []
    current_content = ''
    current_size = 0
    counter = 1

    for line in content.splitlines():
        line_size = len(line.encode('utf-8'))
        if current_size + line_size > max_size:
            output_file_path = os.path.join(output_dir, f'{filename}_{counter}{ext}')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(current_content)
            output_files.append(output_file_path)
            counter += 1
            current_content = ''
            current_size = 0

        current_content += line + '\n'
        current_size += line_size

    # Write the remaining content to the last file
    if current_content:
        output_file_path = os.path.join(output_dir, f'{filename}_{counter}{ext}')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(current_content)
        output_files.append(output_file_path)

    return output_files


download_html(onion_url)

output_dir='scrap\\output'
directory="scrap"
input_files=os.listdir(directory)[0]
input_files="scrap\\"+input_files
try:
    os.mkdir("scrap\\output")
except:
    pass

output_dir="scrap\\output"

break_html(input_files,output_dir)



