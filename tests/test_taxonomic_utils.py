import unittest
from taxonomic_utils import extract_taxonomic_info, preprocess_viral_db
from kmer_utils import BWT

class TestTaxonomicUtils(unittest.TestCase):
    def test_extract_taxonomic_info(self):
        header = "virus [Homo sapiens]"
        taxonomic_info = extract_taxonomic_info(header)
        self.assertEqual(taxonomic_info, "Homo sapiens")
    
    def test_preprocess_viral_db(self):
        viral_sequences = {"virus1 [Homo sapiens]": "GATTACA"}
        bwt_db = preprocess_viral_db(viral_sequences)
        self.assertIn("Homo sapiens", bwt_db)
        
        correct_bwt = BWT("GATTACA").bwt
        self.assertEqual(bwt_db["Homo sapiens"].bwt, correct_bwt)

if __name__ == "__main__":
    unittest.main()
