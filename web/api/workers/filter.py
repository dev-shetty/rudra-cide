from bs4 import BeautifulSoup

# Import HTML file from scrap
with open('scrap/juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.html', 'r', encoding='utf-8') as file:
    html_content = file.read() 

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the image tag
image_tag = soup.find('img')

# Extract the src attribute from the image tag
if image_tag:
    image_link = image_tag.get('src')
    # Format the image link as [imagelink]
    formatted_image_link = f"[{image_link}]"
    # Append it with the url and download the image


    print(formatted_image_link)
