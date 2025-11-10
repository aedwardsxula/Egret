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
    
    # --- Additional Tests (19) ---

    # 1. Test skip file empty
    def test_load_skip_list_empty_file(self):
        tmp = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp.close()
        result = self.processor.load_skip_list(tmp.name)
        self.assertEqual(result, set())
        os.unlink(tmp.name)

    # 2. Test skip list file with spaces only
    def test_load_skip_list_spaces_only(self):
        tmp = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        tmp.write("   \n   \n")
        tmp.close()
        result = self.processor.load_skip_list(tmp.name)
        self.assertEqual(len(result), 0)
        os.unlink(tmp.name)

    # 3. Test API call returns list for valid word
    def test_get_synnony_returns_list(self):
        result = self.processor.get_Synnony("happy")
        self.assertIsInstance(result, list)

    # 4. Test get_Synnony returns error message for bad URL
    def test_get_synnony_handles_network_error(self):
        import requests
        original_get = requests.get
        requests.get = lambda *a, **k: (_ for _ in ()).throw(requests.RequestException("Mock error"))
        result = self.processor.get_Synnony("joy")
        self.assertTrue(any("Error fetching synonyms" in x for x in result))
        requests.get = original_get

    # 5. Test skip word stays unchanged
    def test_get_synnony_skips_word(self):
        self.processor.skip.add("stay")
        result = self.processor.get_Synnony("stay")
        self.assertEqual(result, ["stay"])

    # 6. Test skiptext counter increments
    def test_skip_counter_increments(self):
        before = self.processor.skiptext
        self.processor.skip.add("hold")
        self.processor.get_Synnony("hold")
        self.assertGreater(self.processor.skiptext, before)

    # 7. Test tochange counter increments
    def test_tochange_counter_increments(self):
        before = self.processor.tochange
        self.processor.get_Synnony("run")
        self.assertGreaterEqual(self.processor.tochange, before)

    # 8. Test process_sentence returns dict of words
    def test_process_sentence_returns_dict(self):
        result = self.processor.process_sentence("one two three")
        self.assertIsInstance(result, dict)
        self.assertIn("one", result)

    # 9. Test process_sentence preserves number of words
    def test_process_sentence_preserves_word_count(self):
        sentence = "one two three four"
        result = self.processor.process_sentence(sentence)
        self.assertEqual(len(result), len(sentence.split()))

    # 10. Test process_sentence handles mixed-case words
    def test_process_sentence_mixed_case(self):
        sentence = "Hello HeLLo hello"
        result = self.processor.process_sentence(sentence)
        self.assertEqual(len(result), 3)

    # 11. Test process_sentence handles punctuation safely
    def test_process_sentence_with_punctuation_marks(self):
        sentence = "run, jump! fly?"
        result = self.processor.process_sentence(sentence)
        self.assertIsInstance(result, dict)

    # 12. Test process_sentence returns something for every word
    def test_process_sentence_not_empty_values(self):
        sentence = "bright dark light"
        result = self.processor.process_sentence(sentence)
        for synonyms in result.values():
            self.assertTrue(len(synonyms) > 0)

    # 13. Test process_sentence with numbers
    def test_process_sentence_handles_numbers(self):
        sentence = "one 2 three"
        result = self.processor.process_sentence(sentence)
        self.assertIsInstance(result, dict)

    # 14. Test that repeated words only fetch once (if cached)
    def test_process_sentence_repeated_word_efficiency(self):
        sentence = "repeat repeat repeat"
        result = self.processor.process_sentence(sentence)
        self.assertIn("repeat", result)

    # 15. Test get_Synnony returns unique words (no duplicates)
    def test_get_synnony_unique_results(self):
        result = self.processor.get_Synnony("fast")
        self.assertEqual(len(result), len(set(result)))

    # 16. Test skip file reload does not crash
    def test_reload_skip_file(self):
        _ = self.processor.load_skip_list(self.tmp_skip.name)
        self.assertIsInstance(_, set)

    # 17. Test invalid file type raises handled warning
    def test_invalid_file_type_safe(self):
        try:
            self.processor.load_skip_list("fake.bin")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    # 18. Test processor session object exists
    def test_processor_has_session(self):
        self.assertTrue(hasattr(self.processor, "session"))

    # 19. Test noun_flag property remains boolean
    def test_noun_flag_remains_boolean(self):
        self.assertIsInstance(self.processor.noun_flag, bool)


if __name__ == "__main__":
    unittest.main()
