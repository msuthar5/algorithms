"""
Leetcode #62 Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

24ms faster than 98% of submissions
12.7 MB less than 100% of submissions

Using Dynamic Programming:

Optimal Substructure:
# Unique Paths from:
A[0][0] to A[m-1][n-1] = numUniquePaths(A[m-2][n-1])+numUniquePaths(A[m-1][n-2])
"""
def uniquePaths(m: int, n: int):
    table=[[1]*m for i in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            table[i][j]=table[i][j-1]+table[i-1][j]
    return table[n-1][m-1]
