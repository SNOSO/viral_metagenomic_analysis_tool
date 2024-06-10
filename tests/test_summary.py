import unittest
from summary import create_summary_table

class TestSummary(unittest.TestCase):
    def test_create_summary_table(self):
        identified_viruses = {"Homo sapiens": ["GAT", "TAC"]}
        metrics = {
            "abundance": {"Homo sapiens": 1.0},
            "shannon_index": 0.0,
            "simpson_index": 0.0,
            "richness": 1,
            "evenness": 1.0
        }
        summary_table = create_summary_table(identified_viruses, metrics)
        self.assertTrue("Virus Name" in summary_table.columns)
        self.assertTrue("Shannon Diversity Index" in summary_table.columns)

if __name__ == "__main__":
    unittest.main()
