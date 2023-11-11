"""
##### Problem 2
Retrieve the contents of the sd.deltasd.bc.ca webpage.
Remove all of the HTML and display just the real contents of the page.
"""

import requests
from bs4 import BeautifulSoup

url = "https://sd.deltasd.bc.ca"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    text_content = soup.get_text()
    print(text_content)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")