# imports
from scraper import scrape_website
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
