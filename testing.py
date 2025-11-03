import unittest
from xula import scrape_website

class TestFunction(unittest.TestCase):
    def test_scraper_recipe_website(self):
        result = scrape_website("https://pinchofyum.com/the-best-soft-chocolate-chip-cookies", 
                                "ol", 
                                "class", 
                                "wp-block-list")
        self.assertIsInstance(result, list)
        # self.assertGreater(len(result), 0)
        # self.assertIn("Example Domain", result[0])

    def test_blank_url(self):
        result = scrape_website("", "div")
        self.assertIsInstance(result, str)
        self.assertIn("An error occurred while scraping the website", result)

    def test_invalid_url(self):
        result = scrape_website("htp://invalid-url", "div")
        self.assertIsInstance(result, str)
        self.assertIn("An error occurred while scraping the website", result)

    def test_actual_blank_page(self):
        result = scrape_website("https://example.com/blankpage", "div")
        #self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
        #self.assertEqual(result[0], "Nothing Found")


if __name__ == '__main__':
    unittest.main()