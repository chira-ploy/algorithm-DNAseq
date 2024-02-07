#!/usr/bin/env python

def readFASTA(filename):
    """
    Reads DNA sequences from a FASTA file and concatenates them into a single string.

    Parameters:
    - filename (str): The path to the FASTA file to be read.

    Returns:
    - str: A string representing the concatenated DNA sequences.
    """

    genome = ''
    with open(filename) as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
