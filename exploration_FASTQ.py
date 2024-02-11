#!/usr/bin/env python

def phred33ToQ(qual):
    """
    Convert a Phred quality score encoded in the ASCII format using the Phred+33 encoding scheme to a numeric quality score.

    Args:
    qual (str): The Phred quality score encoded as a single ASCII character.

    Returns:
    int: The numeric quality score corresponding to the input Phred quality score.
    """
    return ord(qual) - 33


def qualityScore_hist(qualityStrings):
    """
    Create a histogram of quality scores from a list of quality strings.

    Args:
    qualityStrings (list): A list of quality strings, where each string represents quality scores of bases in a read.

    Returns:
    list: A histogram of quality scores, where the index represents the quality score and the value represents the frequency.
    """
    # Initialize the histogram list with zeros for quality scores from 0 to 49
    qualityScore_hist = [0] * 50
    
    # Iterate through each read in the list of quality strings
    for read in qualityStrings:
        # Iterate through each Phred quality score in the current read
        for phred in read:
            # Convert the Phred quality score to a numeric quality score
            q = phred33ToQ(phred)
            # Increment the count of the corresponding quality score in the histogram
            qualityScore_hist[q] += 1
    
    return qualityScore_hist


def findGCbyPosition(reads):
    """
    Calculates the GC ratio at each position in a collection of DNA sequences.

    Parameters:
    - reads (list of str): A list containing DNA sequences as strings.

    Returns:
    - list: A list representing the GC ratio at each position in the sequences.
    """

    gc = [0] * 100 #Initialized list for GC counts at each positionin the DNA sequences
    totals = [0] * 100 #Initialized list for total counts at each position
    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            totals[i] += 1  # Increment the count for the corresponding position
            
    # Divide G/C counts by total counts to get the average at each position
    for i in range(len(gc)):
        if totals[i] > 0: 
            gc[i] /= float(totals[i]) # Equivalent to x = x / y
            
    return gc
