#!/usr/bin/env python

# Author = Chiranan Khantham

def editDistance_approximate_matching(x, y):
    """
    Calculate the approximate edit distance between two strings.

    Parameters:
    - x (str): The first string.
    - y (str): The second string.

    Returns:
    - int: The minimum approximate edit distance between the two strings.
    """
    
    # Create distance matrix
    D = []   
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
        
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0
        
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
            
    # Edit distance is the value in the bottom right corner of the matrix
    distance = D[-1] #last row of the matrix
    distance.sort() #all possible alignments are stored in the last row of the matrix
    
    return distance[0]
