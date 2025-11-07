# imports
from scraper import scrape_website
import requests
import json
import sys

# constants & globals (if really needed)
# TODO [All]: Add constants or session objects if required (e.g., skip words, API sessions)
class SynonymProcessor:
    def __init__(self, skip_file='skip.txt', noun_flag=True):
        self.skip = self.load_skip_list(skip_file)
        self.noun_flag = noun_flag
        self.session = requests.session()
        self.skiptext = 0
        self.tochange = 0

    def load_skip_list(self, skip_file):
        try:
            with open(skip_file, 'r') as f:
                return set(line.strip().lower() for line in f if line.strip())
        except FileNotFoundError:
            return set()

# helper functions
# TODO [ Tester @ kyleighharkless]: Implement the logic to fetch synonyms from the thesaurus API
    # This will replace the current pass
    # Example: handle vulgar/informal words, skip list, noun flag
def get_Synnony(word):
    base_url = f"https://api.datamuse.com/words?rel_syn={word}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        synonyms = []
        for item in data:
            synonyms.append(item['word'])
        
        if synonyms:
            return list(set(synonyms)) 
        else:
            return ["Nothing found"]

    except requests.RequestException as e:
        return [f"Error fetching synonyms: {e}"]

# Core Methods
def process_sentence(self,sentence, noun_flag):
    # TODO [Lead @SMAX-byte + Designer @zodagoatfr]: Implement the main sentence processing logic
    # This function should:
    # 1. Split the sentence into 
    words = sentence.split()
     # 2. Call getsynnony() on each word
    # 3. Rebuild the new sentence
    # 4. Return the result
    return[self.get_Synnony(word) for word in words]
    
#  DRIVER / main 
def main():
    # TODO [Lead @SMAX-byte]: Handle command-line arguments (-s, -nonoun) or interactive input
    # TODO [All]: Read skip.txt or other configuration files if needed
    # TODO [All]: Call process_sentence() with proper arguments
    # TODO [All]: Print or save the processed sentence

    print(" Team Egret XULA Driver running...")
    
    # Scrape Centennial Campaign Act
    xula_centennial_campaign = scrape_website("https://www.xula.edu/about/centennial.html",
                                              "span",
                                              "style",
                                              "color: #000000; font-family: verdana, geneva, sans-serif; font-size: 12pt;")
    campaign_impact_paragraph = 2
    print(f"\nXULA's Campaign Impact: \n{xula_centennial_campaign[campaign_impact_paragraph]}\n")

# standard entry point
if __name__ == "__main__":
    main()
