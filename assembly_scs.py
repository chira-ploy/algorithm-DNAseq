#!/usr/bin/env python

import itertools

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


def scs(string_set):
    """
    Finds the shortest common superstring from a given set of strings.

    Parameter:
    - string_set (list): A list of strings from which the shortest common superstring is to be found.

    Returns:
    - str: The shortest common superstring among all permutations of `string_set`, or `None` if no common superstring is found.
    """
    
    shortest_superstring = None
    
    for permutation in itertools.permutations(string_set): # loop through every permutations 
        superstring = permutation[0] #the superstring start with the first string in the permutation list
        
        for i in range(len(string_set) - 1): # -1 because we skip the first string
            overlap_length = overlap(permutation[i], permutation[i+1], min_length=1)
            superstring += permutation[i+1][overlap_length:] #append with the part of the next string which is not overlap
        if shortest_superstring is None or len(superstring) < len(shortest_superstring):
            shortest_superstring = superstring
            
    return shortest_superstring


def scs_list(string_set):
    """
    Find the shortest common superstring(s) of a set of strings.

    Parameters:
    - string_set (list): A list of strings.

    Returns:
    - list: A list containing the shortest common superstring(s) of the input strings.
    """
    
    list_shortest_superstring = []
    shortest_superstring = None
    shortest_superstring_length = float('inf')

    for permutation in itertools.permutations(string_set):
        superstring = permutation[0]
        
        for i in range(len(string_set) - 1):
            overlap_length = overlap(permutation[i], permutation[i + 1], min_length=1)
            superstring += permutation[i + 1][overlap_length:]

        if len(superstring) < shortest_superstring_length:
            shortest_superstring = superstring
            shortest_superstring_length = len(superstring)
            list_shortest_superstring = [shortest_superstring]
        elif len(superstring) == shortest_superstring_length:
            list_shortest_superstring.append(superstring)

    return list_shortest_superstring
