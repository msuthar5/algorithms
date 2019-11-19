"""
Leetcode #64 Minimum Path Sum

Given an MxN matrix, Grid
Find the shortest cost path from Grid[0][0] to Grid[M-1][N-1]
** While the exercise only requires finding SP to Grid[M-1][N-1]
this solution finds the shortest path from Grid[0][0] to any location **

96ms faster than 98.75% of submissions
14.3 MB less than 75% of submissions

Using dynamic Programming
"""
def buildTable(grid,nrows,ncols):
    table=[[None]*ncols for i in range(nrows)]
    table[0][0]=grid[0][0]
    for i in range(1,ncols):
        table[0][i]=table[0][i-1]+grid[0][i]
    for i in range(1,nrows):
        table[i][0]=table[i-1][0]+grid[i][0]
    for i in range(1,nrows):
        for j in range(1,ncols):
            table[i][j]=grid[i][j]+min(table[i][j-1],table[i-1][j])
    return table

def minPathSum(grid):
    nrows,ncols=len(grid),len(grid[0])
    return buildTable(grid,nrows,ncols)[nrows-1][ncols-1]
