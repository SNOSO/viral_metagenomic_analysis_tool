import unittest
from file_parser import parse_file

class TestFileParser(unittest.TestCase):
    def setUp(self):
        self.fastq_content = "@SEQ_ID\nGATTACA\n+\n!!!!!\n"
        with open("test.fastq", "w") as f:
            f.write(self.fastq_content)
        
        self.fasta_content = ">SEQ_ID\nGATTACA\n"
        with open("test.fasta", "w") as f:
            f.write(self.fasta_content)

    def tearDown(self):
        import os
        os.remove("test.fastq")
        os.remove("test.fasta")

    def test_parse_fastq(self):
        sequences, qualities = parse_file("test.fastq")
        self.assertEqual(sequences, ["GATTACA"])
        self.assertEqual(qualities, [[0, 0, 0, 0, 0]])

    def test_parse_fasta(self):
        sequences, _ = parse_file("test.fasta")
        self.assertEqual(sequences, {"SEQ_ID": "GATTACA"})

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            parse_file("non_existent_file.fastq")

if __name__ == "__main__":
    unittest.main()
