import re
from kmer_utils import BWT

def extract_taxonomic_info(header):
    match = re.search(r'\[(.*?)\]', header)
    if match:
        return match.group(1)
    return header  # Return the whole header if no match is found

def preprocess_viral_db(viral_sequences):
    bwt_db = {}
    for header, sequence in viral_sequences.items():
        taxonomic_info = extract_taxonomic_info(header)
        bwt_db[taxonomic_info] = BWT(sequence)
    return bwt_db
