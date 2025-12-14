#!/usr/bin/env python3
"""
Title: Compare Two Text Files (Intersection + Difference)
Author: Nasim Rahmatpour
Date: 2015-08-14
Description:
Compare two text files (one item per line) and write:
1) shared lines (intersection)
2) lines present in file1 but not file2 (difference)

Inputs:
- file1: file1.txt
- file2: file2.txt
Outputs:
- shared.txt
- difference.txt

Usage:
- python compare_list.py

"""

# ---- input files (use relative paths if files are in same folder as script) ----
file1_path = "file1.txt"
file2_path = "file2.txt"

# ---- output files ----
shared_out = "shared.txt"
diff_out = "difference.txt"

# Read + clean lines 
with open(file1_path, "r", encoding="utf-8") as f1:
    set1 = {line.strip() for line in f1 if line.strip()}

with open(file2_path, "r", encoding="utf-8") as f2:
    set2 = {line.strip() for line in f2 if line.strip()}

# Compute shared and difference
shared = set1.intersection(set2)
difference = set1.difference(set2)

# Write outputs 
with open(shared_out, "w", encoding="utf-8") as out:
    for line in sorted(shared):
        out.write(line + "\n")

with open(diff_out, "w", encoding="utf-8") as out:
    for line in sorted(difference):
        out.write(line + "\n")

print(f"File1 lines: {len(set1)}")
print(f"File2 lines: {len(set2)}")
print(f"Shared lines: {len(shared)} -> {shared_out}")
print(f"File1-only lines: {len(difference)} -> {diff_out}")
