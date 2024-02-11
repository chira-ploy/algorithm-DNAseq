#!/usr/bin/env python

#using Boyer Moore + pigeonhole principle

from bm_preproc import BoyerMoore

#run Boyer_Moore Algorithm
def boyer_moore(p, p_bm, t):
      """
      Perform string matching using the Boyer-Moore algorithm.

      Parameters:
      - p (str): The pattern to search for in the text.
      - p_bm (BoyerMoore): The BoyerMoore object preprocessed for the pattern.
      - t (str): The text where the pattern is to be searched.

      Returns:
      - list: A list containing the starting positions of occurrences of the pattern in the text.
      """
                  
      i = 0 #keep track the location on the text
      occurrences = []
      while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
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
      return occurrences

def bm_approximate_matching(p, t, n):
      """
      Find approximate occurrences of a pattern in a text allowing up to 'n' mismatches.

      Parameters:
      - p (str): The pattern to search for in the text.
      - t (str): The text where the pattern is to be searched.
      - n (int): The maximum number of mismatches allowed.

      Returns:
      - list: A list containing the starting positions of approximate occurrences of the pattern in the text.
      """
      
      segment_length = int(round(len(p) / (n+1)))
      all_matches = set()
      for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches = boyer_moore(p[start:end], p_bm, t)
        
        # Check if the match is within bounds
        for m in matches:
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
                
      return list(all_matches)
