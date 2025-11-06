import requests
from bs4 import BeautifulSoup

def scrape_website(url:str , element:str, attribute_name = "div", attribute = None):
    try:
        headers = {"User-Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36")}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')
        scraped_text = ''

        if attribute:
            scraped_text = soup.find_all(element, attrs={attribute_name: attribute})
        else:
            scraped_text = soup.find_all(element)

        return strip_text(scraped_text)

    except Exception as e:
        return (f"An error occurred while scraping the website: {e}")
    
def strip_text(scraped_text):
    stripped_text_list = []

    if scraped_text is False:
        stripped_text_list.append("Nothing Found")
        return stripped_text_list
        
    for text in scraped_text:
        stripped_text_list.append(text.get_text(strip=True))

    return stripped_text_list