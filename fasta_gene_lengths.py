"""
Title: Compute Gene Lengths from FASTA File
Author: Nasim Rahmatpour
Date: 2018-12-08

Description:
    This script reads a FASTA file line by line and calculates the length
    of each gene/transcript by summing the lengths of its sequence lines.
    It reports summary statistics (min, max, average length) and saves
    individual gene lengths to an output text file.

Inputs:
    - FASTA file (e.g. sequences.fasta)
      Header lines start with '>' and sequence lines follow.

Outputs:
    - length_distribution.txt:
        One gene length per line (in base pairs).

Usage:
    python fasta_gene_lengths.py

Notes:
    - Assumes standard FASTA format.
    - Sequence length is calculated ignoring header lines.
"""

# -------------------------------
# File paths
# -------------------------------
input_fasta = "/Users/nasimrahmatpour/Desktop/sequences.fasta"
output_file = "length_distribution.txt"

# -------------------------------
# Read FASTA file
# -------------------------------
with open(input_fasta, "r") as file:
    fh = file.readlines()

NumGenes =0
sequences=[]
lengths=[]

for line in range(len(fh)):
       if fh[line].startswith(">"):
        NumGenes=NumGenes+1 
        genelength=0
        seq=""
   
       else:
        fh[line] = fh[line].rstrip()
        genelength=genelength+len(fh[line])
        seq=seq +fh[line]
        if line!=len(fh)-1:
            if fh[line+1].startswith(">"):
                sequences.append(seq)
                lengths.append(genelength)
        else:
            sequences.append(seq)
            lengths.append(genelength)


# -------------------------------
# Summary statistics
# -------------------------------
average = sum(lengths) / float(len(lengths))
maximum = max(lengths)
minimum = min(lengths)

print("Number of transcripts:", NumGenes)
print("Maximum length:", maximum)
print("Minimum length:", minimum)
print("Average length:", average)

# -------------------------------
# Write output
# -------------------------------
with open(output_file, "w") as f:
    for length in lengths:
        f.write(str(length) + "\n")
