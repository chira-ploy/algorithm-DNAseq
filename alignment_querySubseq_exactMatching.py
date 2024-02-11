#!/usr/bin/env python

def querySubseq_exactMatching(p, t, subseq_index):
    """
    Find occurrences of a pattern in a text using a subsequence index.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.
    - subseq_index (SubseqIndex): The subsequence index of the text constructed using a subsequence indexing method.

    Returns:
    - tuple: A tuple containing two elements:
        - list: A list containing the starting positions of occurrences of the pattern in the text.
        - int: The number of hits found during the subsequence indexing.
    """
    
    k = subseq_index.k 
    ival = subseq_index.ival
    occurrences = []
    hits = 0
    
    for start_index in range(ival):
        for i in subseq_index.query(p[start_index:]):
            hits += 1
            if p[:] == t[i:i + len(p)]:
                occurrences.append(i)
    
    return occurrences, hits
