import unittest
from synonym_processor import SynonymProcessor

class TestSynonymProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = SynonymProcessor()

    def test_initialization_defaults(self):
        self.assertTrue(self.processor.noun_flag)
        self.assertIsInstance(self.processor.skip, set)
        self.assertIsInstance(self.processor.session, object)  # Could be requests.Session
        self.assertEqual(self.processor.skiptext, 0)
        self.assertEqual(self.processor.tochange, 0)
    
    def test_load_skip_list_creates_skip_set(self):
        self.processor.load_skip_list("test_skip.txt")
        self.assertIn("example", self.processor.skip)

    def test_process_sentence_returns_expected_output(self):
        sentence = "The quick brown fox jumps over the lazy dog."
        result = self.processor.process_sentence(sentence, noun_flag=True)
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "")