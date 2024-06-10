import unittest
from alignment import align_and_check_kmers, calculate_metrics
from taxonomic_utils import preprocess_viral_db

class TestAlignment(unittest.TestCase):
    def test_align_and_check_kmers(self):
        query_kmers = {"GAT": 1}
        viral_sequences = {"Homo sapiens": "GATTACA"}
        viral_db = preprocess_viral_db(viral_sequences)
        kmer_size = 3
        alignments, direct_matches = align_and_check_kmers(query_kmers, viral_sequences, viral_db, kmer_size)
        self.assertIn("Homo sapiens", alignments)
        self.assertIn(("GAT", 1), alignments["Homo sapiens"])

    def test_calculate_metrics(self):
        identified_viruses = {"Homo sapiens": ["GAT", "TAC"]}
        metrics = calculate_metrics(identified_viruses)
        self.assertIn("abundance", metrics)
        self.assertIn("shannon_index", metrics)
        self.assertIn("simpson_index", metrics)

if __name__ == "__main__":
    unittest.main()
