#!/usr/bin/env python

# Author: Chiranan Khantham

import bisect

def querySubseq_approximate_matching(p, t, subseq_index, n):
    """
    Find approximate occurrences of a pattern in a text using a subsequence index.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.
    - subseq_index (SubseqIndex): The subsequence index of the text constructed using a subsequence indexing method.
    - n (int): The maximum number of mismatches allowed.

    Returns:
    - tuple: A tuple containing two elements:
        - list: A list containing the starting positions of approximate occurrences of the pattern in the text.
        - list: A list containing the hits found during the subsequence indexing.
    """

    
    k = subseq_index.k 
    ival = subseq_index.ival
    span = subseq_index.span
    all_matches = set()
    hits = []
    
    for start_index in range(ival):
        subseq = p[start_index:][:span:ival]
        i = bisect.bisect_left(subseq_index.index, (subseq, -1))
        
        while i < len(subseq_index.index):
            if subseq_index.index[i][0] != subseq:
                break
            hits.append(subseq_index.index[i][1])
            i += 1
                
     # Check if the match is within bounds
        for m in hits:
            if m < start_index or m-start_index+len(p) > len(t):
                continue
            mismatches = 0
            
            # Check mismatches before the start index
            for j in range(0, start_index):
                if not p[j] == t[m-start_index+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            
            # Check mismatches after the end index
            for j in range(span, len(p)):
                if not p[j] == t[m-start_index+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            
            # Check mismatches in the hit
            for j in range(start_index, span):
                if not p[j] == t[m-start_index+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
                        
            # If total mismatches are within the allowed limit, add the match index to the set 
            # m - start to get the position of text which match with the first offset of pattern
            if mismatches <= n:
                all_matches.add(m - start_index)
                
    return list(all_matches), hits
