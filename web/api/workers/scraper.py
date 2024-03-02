from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from bs4 import BeautifulSoup
import time

onion_url = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'

options = Options()
options.headless = False  # Run WebDriver in headless mode
options.binary_location = "/home/deveesh/Downloads/tor-browser/Browser/firefox"
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9150)  # Tor default SOCKS port

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
        with open(f"scrap/{shorten}.html", "w", encoding="utf-8") as file:
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

download_html(onion_url)
print("Tor HTML page downloaded successfully.")