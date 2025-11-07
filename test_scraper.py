import unittest
from bs4 import BeautifulSoup
from scraper import scrape_website, strip_text

class TestScraperBasics(unittest.TestCase):

    def test_valid_scrape_returns_list(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")  
        self.assertIsInstance(result, list)  

    def test_list_not_empty(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")
        self.assertGreater(len(result), 0)  

    def test_items_are_strings(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")
        self.assertIsInstance(result[0], str)

    def test_strip_text_returns_list(self):
        raw_html = "<div> hello </div><div> world </div>"
        soup = BeautifulSoup(raw_html, "html.parser")
        raw = soup.find_all("div") 

        result = strip_text(raw)
        self.assertIsInstance(result, list)
        self.assertEqual(result, ["hello", "world"])

    def test_scrape_handles_invalid_url(self):
        url = "https://notarealwebsite.xula.fake"
        result = scrape_website(url, "p")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()

