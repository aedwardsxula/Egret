import unittest
from bs4 import BeautifulSoup
from scraper import scrape_website, strip_text

class TestScraperBasics(unittest.TestCase):

    def test_valid_scrape_returns_list(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")   # <p> tags are safe/easy
        self.assertIsInstance(result, list)  # should return a list

    def test_list_not_empty(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")
        self.assertGreater(len(result), 0)  # list should have items

    def test_items_are_strings(self):
        url = "https://www.xula.edu/about/centennial.html"
        result = scrape_website(url, "p")
        # check first element only to keep test simple
        self.assertIsInstance(result[0], str)

    def test_strip_text_returns_list(self):
        raw_html = "<div> hello </div><div> world </div>"
        soup = BeautifulSoup(raw_html, "html.parser")
        raw = soup.find_all("div")  # these are Tag objects

        result = strip_text(raw)
        self.assertIsInstance(result, list)
        self.assertEqual(result, ["hello", "world"])

    def test_scrape_handles_invalid_url(self):
        url = "https://notarealwebsite.xula.fake"
        result = scrape_website(url, "p")
        # beginner-friendly check: just ensure a string error message comes back
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()

