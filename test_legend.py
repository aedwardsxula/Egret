import unittest
from synonym_processor import SynonymProcessor

class TestSynonymProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = SynonymProcessor()
        