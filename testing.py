import unittest
from xula import scrape_website

class TestFunction(unittest.TestCase):
    def test_scraper_recipe_website(self):
        result = scrape_website("https://pinchofyum.com/the-best-soft-chocolate-chip-cookies", 
                                "ol", 
                                "class", 
                                "wp-block-list")
        self.assertIsInstance(result, list) 

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
        self.assertEqual(len(result), 0) # There is no content but it's still scraping something when it shouldn't
        self.assertEqual(result[0], "Nothing Found")
    
    def test_image_scrape(self):
        image_url = "https://images.unsplash.com/photo-1520841852757-e40af9b5bd12?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmlyZHMlMjBleWUlMjB2aWV3fGVufDB8fDB8fHww&fm=jpg&q=60&w=3000"
        attribute = "display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;"
        result = scrape_website(image_url, "img", "style", attribute)
        self.assertEqual(len(result), 0) #Something will be found but it won't be text


if __name__ == '__main__':
    unittest.main()