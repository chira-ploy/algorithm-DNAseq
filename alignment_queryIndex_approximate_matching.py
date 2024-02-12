#!/usr/bin/env python

import bisect

class Index(object):
    """ Holds a substring index for a text T """

    def __init__(self, t, k):
        """ Create index from all substrings of t of length k """
        self.k = k  # k-mer length (k)
        self.index = []
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer

    def query(self, p):
        """ Return index hits for first k-mer of p """
        kmer = p[:self.k]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def queryIndex_approximate_matching(p, t, n):
    """
    Find approximate occurrences of a pattern in a text using an indexed search.

    Parameters:
    - p (str): The pattern to search for in the text.
    - t (str): The text where the pattern is to be searched.
    - n (int): The maximum number of mismatches allowed.

    Returns:
    - tuple: A tuple containing two elements:
        - list: A list containing the starting positions of approximate occurrences of the pattern in the text.
        - int: The total number of hits found during the indexed search.
    """
   
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    t_index = Index(t, segment_length)
    index_hits = 0
    
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        matches = t_index.query(p[start:end])
            
        # Check if the match is within bounds
        for m in matches:
            index_hits += 1
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
                
    return list(all_matches), index_hits
