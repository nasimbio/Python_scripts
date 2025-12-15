#!/usr/bin/env python3
"""
Title: Line-by-Line Comparison Between Large and Small Files
Author: Nasim Rahmatpour
Date: 2015-04-27

Description:
    This script compares two text files line by line:
      - a large reference file ("big")
      - a see a smaller query file ("small")

    For each line in the smaller file, the script searches for a matching
    identifier in the larger file. When a match is found, selected fields
    from both files are written to an output file.

    The comparison is performed using string splitting and exact matching
    of the first column/field.

Inputs:
    - Large file: reference.txt
    - Small file: query.txt

Outputs:
    - shared.txt:
        Tab-delimited file containing matched identifiers and associated
        fields from both input files.

Usage:
    - python line_comparison_between2files.py
"""

# Open input and output files
big = open('/Users/nasimrahmatpour/Desktop/reference.txt', 'r')
small = open('/Users/nasimrahmatpour/Desktop/query.txt', 'r')
file = open('/Users/nasimrahmatpour/Desktop/shared.txt', 'w')

# Read all lines from both files 
b_f = big.readlines()
s_f = small.readlines()

# Loop over each line in the smaller file
for s_line in s_f:
    # Remove newline and split fields by tab
    s_line = s_line.rstrip('\n')
    s_line = s_line.split('\t')

    # Loop over each line in the larger file
    for b_line in b_f:
        # Clean and split the large-file line
        b_line = b_line.strip(' ')
        b_line = b_line.rstrip('\n')
        b_line = b_line.split("*")

        # Compare the first field of both files
        if s_line[0] == b_line[0]:
            # Print matching ID to stdout
            print(b_line[0])

            # Write selected fields from both files to output
            file.write(
                str(s_line[0]) + "\t" +
                str(s_line[1]) + "\t" +
                str(b_line[1]) + "\t" +
                str(b_line[2])
            )
            file.write('\n')

            # Stop scanning the large file once a match is found
            break

# Close output file
file.close()
