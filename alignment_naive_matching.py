#!/usr/bin/env python

def naive_matching(p,t):
    """
    Performs a naive exact matching algorithm to find occurrences of a pattern in a text.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.

    Returns:
    - list: A list containing the starting positions of occurrences of the pattern in the text.
    """
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True # Assume there is a match initially
        for j in range(len(p)):
            if t[i+j] != p[j]: #it checks if the character at position i + j in the text is equal to the character at position j in the pattern. 
                match = False
                break
        if match:
            occurrences.append(i)
            
    return occurrences


def naive_with_counts(p,t):
    """
    Find exact occurrences of a pattern in a text and count the number of alignments and character comparisons.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.

    Returns:
    - tuple: A tuple containing three elements:
        - list: A list containing the starting positions of exact occurrences of the pattern in the text.
        - int: The number of alignments tried.
        - int: The number of character comparisons performed.
    """
    
    occurrences = []
    num_alignments = 0 #the number of alignments tried
    num_character_comparisons = 0 #the number of character comparisons performed 
    
    for i in range(len(t) - len(p) + 1):
        match = True
        num_alignments += 1
        for j in range(len(p)):
            num_character_comparisons += 1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
            
    return occurrences, num_alignments, num_character_comparisons


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t


def naive_with_rc(p, t):
    """
    Performs naive exact matching algorithm on both forward and reverse complement strands.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.

    Returns:
    - tuple: A tuple containing two lists:
        - List of starting positions of occurrences of the pattern in the forward strand.
        - List of starting positions of occurrences of the reverse complement of the pattern.
        """

    # Check forward strand match
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
            
    # Check reverse complement strand match
    occurrences_rc = []
    p_rc = reverseComplement(p)
    for i in range(len(t) - len(p_rc) + 1):
        match_rc = True
        for j in range(len(p_rc)):
            if t[i+j] != p_rc[j]:
                match_rc = False
                break
        if match_rc:
            occurrences_rc.append(i)

    return occurrences, occurrences_rc


def naive_matching_2mm(p,t):
    """
    Finds approximate occurrences of a pattern in a text allowing up to 2 mismatches.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.

    Returns:
    - list: A list containing the starting positions of approximate occurrences of the pattern.
    """
    
    occurrences = []
    k = 2  # Number of allowed mismatches
    
    for i in range(len(t) - len(p) + 1):
        mismatches = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatches += 1
                if mismatches > k:# Break if more than k mismatches are found
                    break
        if mismatches <= k:
            occurrences.append(i)
            
    return occurrences


def count_matched_reads(reads, genome):
    """
    Count the number of reads (first 30 bases/prefix) that match the genome.

    Args:
    reads (list): A list of reads from the genome.
    genome (str): The reference genome to match against.

    Returns:
    tuple: A tuple containing the number of reads matched to the genome and the total number of reads processed.
    """
    numMatched = 0
    n = 0
    for r in reads:
        r = r[0:30]
        matches = naive_matching(r, genome)
        matches.extend(naive_matching(reverseComplement(r), genome))
        n += 1
        if len(matches) > 0:
            numMatched += 1
            
    return numMatched, n
