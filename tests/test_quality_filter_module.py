import unittest
from quality_filter import filter_quality

class TestQualityFilter(unittest.TestCase):
    def test_filter_quality(self):
        sequences = ["GATTACA", "CGTAA"]
        qualities = [[30, 30, 30, 30, 30, 30, 30], [10, 10, 10, 10, 10]]
        threshold = 20
        filtered_sequences = filter_quality(sequences, qualities, threshold)
        self.assertEqual(filtered_sequences, ["GATTACA"])

if __name__ == "__main__":
    unittest.main()
