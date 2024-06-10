# Viral Metagenomic Data Processor and Analysis Tool

This repository contains a Python script for processing viral metagenomic data, specifically designed for bioinformatics and computational biology applications. The script reads FASTQ and FASTA files, filters sequences based on quality scores, creates k-mers, performs sequence alignment using Burrows-Wheeler Transform (BWT), and generates summary statistics. The output is saved in .txt and .csv files, providing valuable insights into viral communities in metagenomic samples.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)


## Features

- Read and parse FASTQ and FASTA files.
- Filter sequences based on quality scores.
- Create k-mers from sequences.
- Perform sequence alignment using Burrows-Wheeler Transform (BWT).
- Extract taxonomic information from sequence headers.
- Calculate summary statistics including abundance, Shannon diversity index, Simpson diversity index, richness, and evenness.
- Export summary tables to Excel and text files.

## Requirements

- Python 3.6 or higher
- collections
- itertools
- numpy
- openpyxl
- os
- pandas
- re


## Installation

1. Clone the repository:

```sh
git clone https://github.com/SNOSO/viral_metagenomic_analysis_tool.git
cd viral_metagenomic_analysis_tool
```

2. Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # if on Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

you may also install the required packages manually using the following commands:
```sh
pip install numpy
pip install pandas
pip install openpyxl
pip install requests
```

## Usage

### Interactive Mode

Run the script in interactive mode:

```sh
python main.py
```

You will be prompted to enter the paths to the input files, quality threshold, k-mer size, and output directory.

## Example:

```sh
Enter the path to the FASTQ file: path/to/subset.fastq
Enter the path to the FASTA file: path/to/BVBRC_genome_sequence.fasta
Enter the quality threshold (Phred score): 25
Enter the k-mer size: 5
Enter the output directory: path/to/output/dir/
```

## Testing

To run the unit tests, use the following command:

```sh
python -m unittest discover -s tests
```

## Input files
There are two input files required for the script to run: a FASTQ file containing the metagenomic reads and a FASTA file containing the viral database sequences. The FASTQ file should contain the raw sequencing reads, while the FASTA file should contain the viral sequences to be aligned against the reads. The script will parse these files and process the data accordingly.
Included in this repository is a FASTQ file named `subset.fastq` containing a subset of metagenomic reads and a FASTA file named `BVBRC_genome_sequence.fasta` containing viral sequences from the Broad Viral Bioinformatics Resource Center (BVBRC). These files can be used to test the script.

## File Descriptions

- `main.py`: The main script to process viral metagenomic data.
- `file_parser.py`: Functions for parsing FASTQ and FASTA files.
- `quality_filter.py`: Functions for filtering sequences based on quality scores.
- `kmer_utils.py`: Functions for creating k-mers and BWT processing.
- `taxonomic_utils.py`: Functions for extracting taxonomic information and preprocessing the viral database.
- `alignment.py`: Functions for aligning k-mers and calculating metrics.
- `summary.py`: Functions for creating the summary table.
- `tests/`: Directory containing unit tests for the modules.
- `requirements.txt`: List of required Python packages.
- `subset.fastq`: Example FASTQ file containing metagenomic reads.
- `BVBRC_genome_sequence.fasta`: Example FASTA file containing viral sequences from the BVBRC.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Citations
1. Broad Viral Bioinformatics Resource Center. (n.d.). Taxonomy overview for SARS-CoV-2. Retrieved June 7, 2024, from https://www.bv-brc.org/view/Taxonomy/2697049#view_tab=overview
2. openpyxl: openpyxl contributors. (2010). openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files. Available at: https://openpyxl.readthedocs.io/
3. pandas: McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, 51-56.
4. National Center for Biotechnology Information. (n.d.). Run Browser for SRR12464727. Retrieved June 7, 2024, from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&page_size=10&acc=SRR12464727&display=metadata
5. numpy: Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., ... & Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585(7825), 357-362.
