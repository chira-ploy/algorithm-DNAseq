#!usr/bin/env python

# Description: 
# This function serves as a verification step to confirm the correctness of hits obtained 
# from previous Index and query functions. It compares patterns against a reference text 
# using an index structure, ensuring alignment and similarity to validate the hits. 

def queryIndex_exactMatching(p, t, index):
    """
    Query an index to verify the correctness of hits.
    
    Args:
    - p: pattern string
    - t: reference text string
    - index: index object
    
    Returns:
    - offsets: list of offsets where matches occur
    """
    
    k = index.k #retrieves the length of k from the index object
    offsets = [] #list of offsets where it matches
    
    for i in index.query(p): #This loop iterates over the positions in the text where occurrences of the pattern p were found using the query method from the index object
        if p[k:] == t[i+k:i+len(p)]:#the substring of t from position i+k to i+len(p) (inclusive) is equal to the remaining part of the pattern p starting from position k
            offsets.append(i)
            
    return offsets
