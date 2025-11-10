# imports
from scraper import scrape_website
import requests
import json
import sys
import requests
import argparse

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
   if not sentence.strip():
        print("No words to process.")
        return ""
    # This function should:
    # 1. Split the sentence into 
    words = sentence.split()
     # 2. Call getsynnony() on each word
    # 3. Rebuild the new sentence
    # 4. Return the result
    return[self.get_Synnony(word) for word in words]
    
class ChangeTracker:
    def __init__(self):
        self.total_words = 0
        self.changed_words = 0

    def record(self, original, new):
        self.total_words += 1
        if original != new:
            self.changed_words += 1

    def summary(self):
        return f"Words changed: {self.changed_words} out of {self.total_words}"

    def reset(self):
        self.total_words = 0
        self.changed_words = 0


#  DRIVER / main 
def main():
    # TODO [Lead @SMAX-byte]: Handle command-line arguments (-s, -nonoun) or interactive input

    print(" Team Egret XULA Driver running...")
    parser = argparse.ArgumentParser(description="Process a sentence to find synonyms.")
    parser.add_argument('-s', '--sentence', type=str, help='Input sentence to process')
    parser.add_argument('-nonoun', '--nonoun', action='store_true', help='Skip noun processing')
    args = parser.parse_args()
     # TODO [All]: Read skip.txt or other configuration files if needed
    procesor = SynonymProcessor(noun_flag=not args.nonoun)

     # TODO [All]: Call process_sentence() with proper arguments
    if args.sentence:
        result = procesor.process_sentence(args.sentence, procesor.noun_flag)
     # TODO [All]: Print or save the processed sentence
        print("Processed Sentence Synonyms:")
        for word_synonyms in result:
            print(word_synonyms)

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
