import os

def parse_file(input_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    sequences = []
    qualities = []
    
    if input_file.endswith('.fastq'):
        with open(input_file, 'r') as f:
            while True:
                header = f.readline().strip()
                if not header:
                    break
                seq = f.readline().strip().upper()  # Convert to uppercase
                f.readline()  # Plus line
                qual = f.readline().strip()
                quality = [ord(char) - 33 for char in qual]
                sequences.append(seq)
                qualities.append(quality)
        return sequences, qualities
    
    elif input_file.endswith('.fasta'):
        sequences_dict = {}
        with open(input_file, 'r') as f:
            current_header = None
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    current_header = line[1:]
                    sequences_dict[current_header] = ''
                else:
                    sequences_dict[current_header] += line.upper()  # Convert to uppercase
        return sequences_dict, None

    else:
        raise ValueError("Unsupported file format. Please provide a FASTQ or FASTA file.")
