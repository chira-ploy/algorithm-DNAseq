#!/usr/bin/env python

def readFASTQ(filename):
    """
    Reads data from a FASTQ file and extracts sequence information.

    Parameters:
    - filename (str): The path to the FASTQ file to be read.

    Returns:
    - tuple: A tuple containing two lists:
        - List of DNA or RNA sequences (strings).
        - List of corresponding quality scores for each sequence (strings).
    """

    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline() # skip name line
            seq = fh.readline().rstrip() # read base sequence
            fh.readline() # skip placeholder line
            qual = fh.readline().rstrip() #base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
            
    return sequences, qualities
