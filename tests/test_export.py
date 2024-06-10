import os
import pandas as pd
from file_parser import parse_file
from quality_filter import filter_quality
from kmer_utils import create_kmers
from taxonomic_utils import extract_taxonomic_info, preprocess_viral_db
from alignment import align_and_check_kmers, calculate_metrics
from summary import create_summary_table

def main(fastq_file_path, fasta_file_path, quality_threshold, kmer_size):
    sequences, qualities = parse_file(fastq_file_path)
    filtered_sequences = filter_quality(sequences, qualities, quality_threshold)
    query_kmers = create_kmers(filtered_sequences, kmer_size)
    viral_sequences, _ = parse_file(fasta_file_path)
    viral_sequences = {extract_taxonomic_info(header): seq for header, seq in viral_sequences.items()}
    bwt_db = preprocess_viral_db(viral_sequences)
    alignments, direct_matches = align_and_check_kmers(query_kmers, viral_sequences, bwt_db, kmer_size)
    
    metrics = calculate_metrics(alignments)
    summary_table = create_summary_table(alignments, metrics)
    
    return summary_table

def export_summary_table(summary_table, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    excel_path = os.path.join(output_dir, "summary.xlsx")
    txt_path = os.path.join(output_dir, "summary.txt")
    
    # Export to Excel
    summary_table.to_excel(excel_path, index=False)
    print(f"Summary table exported to {excel_path}")
    
    # Export to txt
    with open(txt_path, 'w') as txt_file:
        txt_file.write(summary_table.to_string(index=False))
    print(f"Summary table exported to {txt_path}")

if __name__ == "__main__":
    # Interactive user inputs
    fastq_file = input("Enter the path to the FASTQ file: ")
    fasta_file = input("Enter the path to the FASTA file containing viral sequences: ")
    quality_threshold = int(input("Enter the quality threshold for filtering sequences: "))
    kmer_size = int(input("Enter the size of the k-mers to create: "))
    output_dir = input("Enter the directory to save the summary files: ")
    
    summary_table = main(fastq_file, fasta_file, quality_threshold, kmer_size)
    export_summary_table(summary_table, output_dir)
