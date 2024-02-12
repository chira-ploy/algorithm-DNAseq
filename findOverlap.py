#!/usr/bin/env python

from itertools import permutations

def overlap(a, b, min_length=3):
    """
    Calculate the overlap length between two strings.

    Parameters:
    - a (str): The first string.
    - b (str): The second string.
    - min_length (int): The minimum length of overlap required. Default is 3.

    Returns:
    - int: The length of the longest suffix of 'a' matching a prefix of 'b'
           that is at least 'min_length' characters long. If no such overlap
           exists, return 0.
    """
    
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
        

def naive_overlap_map(reads, k):
    """
    Find overlaps between reads using a naive approach.

    Parameters:
    - reads (list): A list of strings representing reads.
    - k (int): The minimum length of overlap required.

    Returns:
    - dict: A dictionary containing the pairs of reads as keys and their
            overlap lengths as values.
    """
    
    olaps = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps


def overlap_all_pairs(reads, k):
    """
    Find overlaps among all pairs of reads.

    Parameters:
    - reads (list): A list of strings representing reads.
    - k (int): The length of k-mers used for finding overlaps.

    Returns:
    - tuple: A tuple containing two elements:
             1. A list of tuples representing pairs of reads that overlap.
             2. A set containing reads that have overlaps.
    """
    
    kmer_dict = {}
    overlaps_pair = []
    count_overlap_reads = set()
    
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i + k]
            if kmer not in kmer_dict:
                kmer_dict[kmer] = set()
            kmer_dict[kmer].add(read)
        
    for read in reads:
        current_kmer_set = kmer_dict[read[-k:]]
        for kmer_read in current_kmer_set:
            if read != kmer_read:
                overlap_length = overlap(read, kmer_read, min_length=k)
                if overlap_length > 0:
                    overlaps_pair.append((read, kmer_read))
                    if read not in count_overlap_reads:
                        count_overlap_reads.add(read)
                    
    return overlaps_pair, count_overlap_reads
