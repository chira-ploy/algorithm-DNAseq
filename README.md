# DNA Sequencing Data Analysis

This repository contains Python code for analyzing DNA sequencing data, which I learned from the Coursera course "Algorithms for DNA Sequencing" offered by Johns Hopkins University. The code focuses on solving two main challenges: the read alignment problem and the assembly problem.

## Read Alignment Problem

1. Naive Exact Matching Algorithm (Online Algorithm) <br>
   The naive exact matching algorithm is a simple and flexible approach for finding patterns (short reads) in text (reference genome). While not the fastest, it provides a foundational understanding of pattern matching.

2. Boyer-Moore (Online Algorithm)<br>
   Boyer-Moore is a highly efficient exact matching algorithm used in bioinformatics for comparing a pattern against a text from right to left. It preprocesses the template (t), enhancing search speed significantly. The algorithm achieves efficiency through strategic optimizations, including:
    - Bad character rule: Adjusts the pattern to align the rightmost occurrence of a mismatched character in the pattern with the text.
    - Good suffix rule: Expedites search by identifying the longest matching suffix of the pattern and a prefix of the text.

3. Index Assisted Algorithms (Offline Algorithm) <br>
   Index Assisted Algorithms employ pre-processing steps to construct indexes that facilitate efficient pattern matching and verification during the alignment process. These algorithms are typically executed offline, meaning that the index is constructed beforehand and used during the alignment process. Two common types of index assisted algorithms are:
    - K-mer Index and Binary Search: This approach involves partitioning the reference sequence into overlapping k-mers and constructing an index based on these k-mers. Binary search is then used to quickly locate potential matches for query sequences within the index, significantly reducing search time.
    - Subsequence Index: In this method, the reference sequence is divided into subsequences of fixed length. Each subsequence is indexed, enabling rapid identification of potential matches for query sequences. This indexing strategy enhances search capabilities, particularly for longer query sequences or sequences with repetitive patterns.

### Note 
The concepts of the pigeonhole principle and approximate matching can significantly impact the optimization and design of various DNA alignment algorithms. 

- Pigeonhole Principle is a fundamental concept in combinatorics that states if you have more "pigeons" than "pigeonholes," then at least one pigeonhole must contain more than one pigeon. The pigeonhole principle acts as a bridge for utilizing exact matching algorithms effectively. By dividing the pattern into partitions and using exact matching algorithms, we can find approximate matches. This approach enables efficient verification of occurrences with up to the maximum allowed differences.

- Approximate Matching in DNA alignment refers to the process of finding similarities or matches between DNA sequences while allowing for variations or errors. In DNA alignment, it's common to encounter sequences that are not identical but share similarities due to mutations, insertions, deletions, or other genetic variations. Two common metrics used for approximate matching are:
   - Hamming Distance: This metric measures the number of positions at which corresponding symbols differ between two strings of the same length. It is limited to substitutions only and requires strings of equal size.
   - Edit Distance: Unlike Hamming Distance, Edit Distance considers substitutions, deletions, and insertions. It quantifies the minimum number of operations required to transform one string into another. This comprehensive metric provides a broader perspective on sequence similarity, encompassing a wider range of variations.

## Assembly Problem

1. Shortest Common Superstring <br>
   This algorithm employs overlap-layout-consensus (OLC) assembly to find the shortest common superstring. While effective, it can be slow due to the exhaustive nature of testing possible orderings.

2. Greedy Shortest Common Superstring <br>
   The greedy shortest common superstring algorithm proceeds in rounds, selecting edges with the highest label number for merging nodes. Ties are resolved to ensure a unique superstring.

3. De Bruijn Graph Based (DBG) Assembly <br>
   DBG assembly represents one edge per k-mer and one node per distinct k-1-mer. By traversing each edge exactly once, the original genome sequence can be reconstructed. This method is efficient for handling large datasets and is widely used in genome assembly due to its scalability and effectiveness in capturing repetitive regions and sequencing errors.

## Acknowledgments
Special thanks to the Coursera course "Algorithms for DNA Sequencing" offered by Johns Hopkins University.
