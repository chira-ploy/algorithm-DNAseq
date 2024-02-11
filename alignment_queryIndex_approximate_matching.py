#!/usr/bin/env python

# Author: Chiranan Khantham

import bisect

def queryIndex_approximate_matching(p, t, t_index, n):
    """
    Find approximate occurrences of a pattern in a text using an indexed search.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.
    - t_index (Index): The index of the text constructed using an indexing method.
    - n (int): The maximum number of mismatches allowed.

    Returns:
    - tuple: A tuple containing two elements:
        - list: A list containing the starting positions of approximate occurrences of the pattern in the text.
        - list: A list containing the hits found during the indexed search.
    """
        
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        kmer = p[start:end]
        
        i = bisect.bisect_left(t_index.index, (kmer, -1))
        hits = []
        while i < len(t_index.index):
            if t_index.index[i][0] != kmer:
                break
            hits.append(t_index.index[i][1])
            i += 1
            
        # Check if the match is within bounds
        for m in hits:
            if m < start or m-start+len(p) > len(t):
                continue
            mismatches = 0
            
            # Check mismatches before the start index
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            
            # Check mismatches after the end index
            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
                        
            # If total mismatches are within the allowed limit, add the match index to the set 
            # m - start to get the position of text which match with the first offset of pattern
            if mismatches <= n:
                all_matches.add(m - start)
                
    return list(all_matches), hits
