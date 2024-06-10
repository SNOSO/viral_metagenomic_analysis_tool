import math
from collections import defaultdict

def align_and_check_kmers(query_kmers, viral_sequences, viral_db, kmer_size):
    alignments = defaultdict(list)
    direct_matches = defaultdict(list)

    for virus, bwt in viral_db.items():
        if virus in viral_sequences:
            sequence = viral_sequences[virus]
            for kmer, count in query_kmers.items():
                if len(kmer) != kmer_size:
                    continue
                
                # Check direct presence in the sequence
                if kmer in sequence:
                    direct_matches[virus].append(kmer)
                
                # Perform BWT count
                matches = bwt.count(kmer)
                if matches > 0:
                    alignments[virus].append((kmer, matches))

    return alignments, direct_matches

def calculate_abundance(identified_viruses):
    total_sequences = sum(len(kmers) for kmers in identified_viruses.values())
    abundance = {virus: len(kmers) / total_sequences for virus, kmers in identified_viruses.items()}
    return abundance

def shannon_diversity_index(abundance):
    return -sum(p * math.log(p) for p in abundance.values() if p > 0)

def simpson_diversity_index(abundance):
    return 1 - sum(p**2 for p in abundance.values())

def richness(identified_viruses):
    return len(identified_viruses)

def evenness(abundance):
    shannon_index = shannon_diversity_index(abundance)
    max_shannon_index = math.log(len(abundance)) if len(abundance) > 0 else 1
    return shannon_index / max_shannon_index if max_shannon_index != 0 else 0

def calculate_metrics(identified_viruses):
    abundance = calculate_abundance(identified_viruses)
    shannon_index = shannon_diversity_index(abundance)
    simpson_index = simpson_diversity_index(abundance)
    richness_value = richness(identified_viruses)
    evenness_value = evenness(abundance)
    
    metrics = {
        "abundance": abundance,
        "shannon_index": shannon_index,
        "simpson_index": simpson_index,
        "richness": richness_value,
        "evenness": evenness_value
    }
    
    return metrics
