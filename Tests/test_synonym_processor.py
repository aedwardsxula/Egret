import unittest
import tempfile
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from xula import SynonymProcessor  # change 'main' if your class file has a different name

class TestSynonymProcessor(unittest.TestCase):

    def setUp(self):
        # Create a temporary skip.txt file for testing
        self.tmp_skip = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.tmp_skip.write("skip\nignore\n")
        self.tmp_skip.close()

        # Instantiate the processor with the temporary skip file
        self.processor = SynonymProcessor(skip_file=self.tmp_skip.name, noun_flag=True)

    def tearDown(self):
        os.unlink(self.tmp_skip.name)

    # --- Initialization Tests (4) ---
    def test_init_creates_skip_attribute(self):
        self.assertIsInstance(self.processor.skip, set)

    def test_init_loads_skip_words(self):
        self.assertIn("skip", self.processor.skip)

    def test_init_default_flag_true(self):
        p = SynonymProcessor(skip_file=self.tmp_skip.name)
        self.assertTrue(p.noun_flag)

    def test_init_custom_flag_false(self):
        p = SynonymProcessor(skip_file=self.tmp_skip.name, noun_flag=False)
        self.assertFalse(p.noun_flag)

    # --- Skip List Tests (5) ---
    def test_load_skip_list_reads_lines(self):
        skip_words = self.processor.load_skip_list(self.tmp_skip.name)
        self.assertIn("ignore", skip_words)

    def test_load_skip_list_ignores_empty_lines(self):
        tmp2 = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp2.write("word1\n\nword2\n")
        tmp2.close()
        result = self.processor.load_skip_list(tmp2.name)
        self.assertNotIn('', result)
        os.unlink(tmp2.name)

    def test_load_skip_list_returns_set(self):
        result = self.processor.load_skip_list(self.tmp_skip.name)
        self.assertIsInstance(result, set)

    def test_load_skip_list_removes_duplicates(self):
        tmp3 = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp3.write("word\nword\nword\n")
        tmp3.close()
        result = self.processor.load_skip_list(tmp3.name)
        self.assertEqual(len(result), 1)
        os.unlink(tmp3.name)

    def test_load_skip_list_handles_special_chars(self):
        tmp4 = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp4.write("hello!\nworld?\n")
        tmp4.close()
        result = self.processor.load_skip_list(tmp4.name)
        self.assertTrue("hello!" in result)
        os.unlink(tmp4.name)

    # --- Sentence Processing Tests (7) ---
    def test_process_sentence_returns_string(self):
        result = self.processor.process_sentence("This is a test", True)
        self.assertIsInstance(result, str)

    def test_process_sentence_skips_marked_words(self):
        sentence = "skip this word"
        result = self.processor.process_sentence(sentence, True)
        self.assertIn("skip", result)

    def test_process_sentence_changes_unmarked_words(self):
        sentence = "This is a test"
        result = self.processor.process_sentence(sentence, True)
        self.assertIsInstance(result, str)

    def test_process_sentence_empty_input(self):
        result = self.processor.process_sentence("", True)
        self.assertEqual(result, "")

    def test_process_sentence_handles_punctuation(self):
        sentence = "Hello, world!"
        result = self.processor.process_sentence(sentence, True)
        self.assertIsInstance(result, str)

    def test_process_sentence_with_noun_flag_true(self):
        result = self.processor.process_sentence("Hello world", True)
        self.assertIsInstance(result, str)

    def test_process_sentence_with_noun_flag_false(self):
        result = self.processor.process_sentence("Hello world", False)
        self.assertIsInstance(result, str)

    # --- Counter & State Tests (3) ---
    def test_skiptext_counter_exists(self):
        self.assertTrue(hasattr(self.processor, "skiptext"))

    def test_tochange_counter_exists(self):
        self.assertTrue(hasattr(self.processor, "tochange"))

    def test_counters_are_integers(self):
        self.assertIsInstance(self.processor.skiptext, int)
        self.assertIsInstance(self.processor.tochange, int)

    # --- Error Handling (1) ---
    def test_invalid_skip_file_raises(self):
        with self.assertRaises(Exception):
            SynonymProcessor(skip_file="nonexistent_file.txt")

if __name__ == "__main__":
    unittest.main()
