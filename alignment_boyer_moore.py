#!/usr/bin/env python

from bm_preproc import BoyerMoore

def boyer_moore_with_counts(p, p_bm, t):
    """
    Perform Boyer-Moore matching and count the number of alignments and character comparisons.

    Parameters:
    - p (str): The pattern to search for in the text.
    - p_bm (BoyerMoore): The BoyerMoore object preprocessed for the pattern.
    - t (str): The text where the pattern is to be searched.

    Returns:
    - tuple: A tuple containing three elements:
        - list: A list containing the starting positions of occurrences of the pattern in the text.
        - int: The number of alignments tried.
        - int: The number of character comparisons performed.
    """
    
    i = 0
    occurrences = []
    num_alignments = 0 #the number of alignments tried
    num_character_comparisons = 0 #the number of character comparisons performed 
    
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        num_alignments += 1
        
        for j in range(len(p)-1, -1, -1):
            num_character_comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
                
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
        
    return occurrences, num_alignments, num_character_comparisons
