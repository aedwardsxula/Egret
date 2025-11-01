# imports
import requests
from bs4 import BeautifulSoup
import json
import sys

# constants & globals (if really needed)
# TODO [All]: Add constants or session objects if required (e.g., skip words, API sessions)

# helper functions
def getsynnony(word):
    # TODO [ Tester @ kyleighharkless]: Implement the logic to fetch synonyms from the thesaurus API
    # This will replace the current pass
    # Example: handle vulgar/informal words, skip list, noun flag
    pass  # placeholder for future implementation

# Core Methods
def process_sentence(sentence, noun_flag):
    # TODO [Lead @SMAX-byte + Designer @zodagoatfr]: Implement the main sentence processing logic
    # This function should:
    # 1. Split the sentence into words
    # 2. Call getsynnony() on each word
    # 3. Rebuild the new sentence
    # 4. Return the result
    pass  # placeholder for future implementation

#  DRIVER / main 
def main():
    # TODO [Lead @SMAX-byte]: Handle command-line arguments (-s, -nonoun) or interactive input
    # TODO [All]: Read skip.txt or other configuration files if needed
    # TODO [All]: Call process_sentence() with proper arguments
    # TODO [All]: Print or save the processed sentence

    print(" Team Egret XULA Driver running...")
    
    xula_centennial_campaign = scrape_website("https://www.xula.edu/about/centennial.html",
                                              "span",
                                              "style",
                                              "color: #000000; font-family: verdana, geneva, sans-serif; font-size: 12pt;")
    print(xula_centennial_campaign)

# Scrape Centennial Campaign Act
def scrape_website(url:str , element:str, attribute_name = "div", attribute = None):
    try:
        headers = {"User-Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36")}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')

        scraped_text = ''

        if attribute:
            scraped_text = soup.find(element, attrs={attribute_name: attribute})
        else:
            soup.find(element)

        return print_scraped_text(scraped_text)

    except Exception as e:
        return (f"An error occurred while scraping the website: {e}")
    
def print_scraped_text(scraped_text):
    if scraped_text:
        return scraped_text
    else:
        return "Nothing found."
    
# def strip_text(scraped_text):
#     stripped_text = []
#     for text in scraped_text:
#         # print(text.get_text(strip=True))
#         return text.append(stripped_text)

# standard entry point
if __name__ == "__main__":
    main()
