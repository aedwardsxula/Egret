import unittest
from xula import SynonymProcessor

class TestSynonymProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = SynonymProcessor()

    def test_initialization_defaults(self):
        self.assertTrue(self.processor.noun_flag)
        self.assertIsInstance(self.processor.skip, set)
        self.assertIsInstance(self.processor.session, object)
        self.assertEqual(self.processor.skiptext, 0)
        self.assertEqual(self.processor.tochange, 0)
    
    def test_load_skip_list_creates_skip_set(self):
        self.processor.load_skip_list("test_skip.txt")
        self.assertIn("example", self.processor.skip)

    def test_load_skip_list_empty_file(self):
        self.processor.load_skip_list("empty_skip.txt")  
        self.assertEqual(len(self.processor.skip), 0)

    def test_load_skip_list_with_duplicates(self):
        self.processor.load_skip_list("duplicate_skip.txt")
        self.assertEqual(len(self.processor.skip), len(set(self.processor.skip)))

    def test_process_sentence_empty_string(self):
        result = self.processor.process_sentence("", noun_flag=True)
        self.assertEqual(result, "")


    def test_process_sentence_returns_expected_output(self):
        sentence = "The quick brown fox jumps over the lazy dog."
        result = self.processor.process_sentence(sentence, noun_flag=True)
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "")

    def test_process_sentence_respects_noun_flag(self):
        sentence = "Cats chase mice."
        result_with_noun = self.processor.process_sentence(sentence, noun_flag=True)
        result_without_noun = self.processor.process_sentence(sentence, noun_flag=False)
        self.assertNotEqual(result_with_noun, result_without_noun)

    def test_process_sentence_skips_words(self):
        self.processor.skip = {"fox", "dog"}
        sentence = "The quick brown fox jumps over the lazy dog."
        result = self.processor.process_sentence(sentence, noun_flag=True)
        self.assertNotIn("fox", result)
        self.assertNotIn("dog", result)

    def test_custom_initialization(self):
        custom_processor = SynonymProcessor(skip_file="custom.txt", noun_flag=False)
        self.assertFalse(custom_processor.noun_flag)
        self.assertIsInstance(custom_processor.skip, set)


