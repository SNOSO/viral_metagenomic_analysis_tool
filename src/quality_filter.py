import numpy as np

def filter_quality(sequences, qualities, threshold):
    filtered_sequences = []
    for seq, qual in zip(sequences, qualities):
        mean_quality_score = np.mean(qual)
        if mean_quality_score >= threshold:
            filtered_sequences.append(seq)
    return filtered_sequences
