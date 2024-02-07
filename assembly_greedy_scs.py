#!/usr/bin/env python

def overlap(a, b, min_length=3):
    """
    Return the length of the longest suffix of string 'a' matching
    a prefix of string 'b' that is at least 'min_length' characters long.
    If no such overlap exists, return 0.

    Parameters:
    - a (str): First string.
    - b (str): Second string.
    - min_length (int): Minimum length of overlap required.

    Returns:
    - int: Length of the longest overlap between 'a' and 'b'.
    """
    
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def pick_maximal_overlap_kmer(reads, k):
    """
    Find a pair of reads with the maximal overlap among all pairs of reads.

    Parameters:
    - reads (list): A list of reads.
    - k (int): Length of k-mer to use for finding overlaps.

    Returns:
    - tuple: A tuple containing the two reads with the maximal overlap and the
             length of the overlap.
    """
    
    reada, readb = None, None
    best_overlap_length = 0
    
    kmer_dict = {}
    
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
                if overlap_length > best_overlap_length:
                    reada, readb = read, kmer_read
                    best_overlap_length = overlap_length
            
    return reada, readb, best_overlap_length

def greedy_scs(reads, k):
    """
    Construct a shortest common superstring (SCS) using a greedy algorithm.

    Parameters:
    - reads (list): A list of reads.
    - k (int): Length of k-mer to use for finding overlaps.

    Returns:
    - str: The shortest common superstring constructed from the input reads.
    """
    
    reada, readb, overlap_length = pick_maximal_overlap_kmer(reads, k)
    while overlap_length > 0:
        reads.remove(reada)
        reads.remove(readb)
        reads.append(reada + readb[overlap_length:])
        reada, readb, overlap_length = pick_maximal_overlap_kmer(reads, k)
        
    return ''.join(reads) #the remaining reads will be those that are not overlap, so we merge them
