import unittest
from kmer_utils import create_kmers, BWT

class TestKmerUtils(unittest.TestCase):
    def test_create_kmers(self):
        sequences = ["GATTACA"]
        kmer_size = 3
        kmers = create_kmers(sequences, kmer_size)
        expected_kmers = {'GAT': 1, 'ATT': 1, 'TTA': 1, 'TAC': 1, 'ACA': 1}
        self.assertEqual(kmers, expected_kmers)

    def test_bwt(self):
        bwt = BWT("GATTACA")
        self.assertEqual(bwt.bwt, "ACTGA$TA")  # Corrected expected BWT

if __name__ == "__main__":
    unittest.main()
