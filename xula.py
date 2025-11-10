# imports
from scraper import scrape_website
import json
import sys

# constants & globals (if really needed)
# TODO [All]: Add constants or session objects if required (e.g., skip words, API sessions)

# class SynonymProcessor:
#     def __init__(self, skip_file='skip.txt', noun_flag=True):
#         self.skip = self.load_skip_list(skip_file)
#         self.noun_flag = noun_flag
#         self.session = requests.session()
#         self.skiptext = 0
#         self.tochange = 0

#     def load_skip_list(self, skip_file):
#         try:
#             with open(skip_file, 'r') as f:
#                 return set(line.strip().lower() for line in f if line.strip())
#         except FileNotFoundError:
#             return set()
        
import random
import requests

class SynonymProcessor:
    def __init__(self, skip_file='skip.txt', noun_flag=True, change_rate=1.0):
        self.skip = self.load_skip_list(skip_file)
        self.noun_flag = noun_flag
        self.session = requests.session()
        self.skiptext = 0
        self.tochange = 0
        self.change_rate = change_rate  # percentage of words to change (0.0–1.0)

    def load_skip_list(self, skip_file):
        try:
            with open(skip_file, 'r') as f:
                return set(line.strip().lower() for line in f if line.strip())
        except FileNotFoundError:
            return set()

    def process_sentence(self, sentence, noun_flag=None):
        if noun_flag is None:
            noun_flag = self.noun_flag

        words = sentence.split()
        new_words = []

        for word in words:
            # roll the dice: should we change this word?
            if random.random() < self.change_rate:
                new_words.append(self.getsynnony(word) or word)
            else:
                new_words.append(word)

        return " ".join(new_words)


# helper functions
def getsynnony(word):
    # TODO [ Tester @ kyleighharkless]: Implement the logic to fetch synonyms from the thesaurus API
    # This will replace the current pass
    # Example: handle vulgar/informal words, skip list, noun flag
    pass  # placeholder for future implementation

# Core Methods
def process_sentence(self,sentence, noun_flag):
    # TODO [Lead @SMAX-byte + Designer @zodagoatfr]: Implement the main sentence processing logic
    # This function should:
    # 1. Split the sentence into 
    words = sentence.split()
     # 2. Call getsynnony() on each word
    # 3. Rebuild the new sentence
    # 4. Return the result
    return[self.getsynnony(word) for word in words]
    

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
    
    sentence = input("Enter a sentence: ")
    processor = SynonymProcessor(skip_file="skip.txt", noun_flag=True, change_rate=0.3)
    new_sentence = processor.process_sentence(sentence)
    print("Processed sentence:", new_sentence)


# standard entry point
if __name__ == "__main__":
    main()
