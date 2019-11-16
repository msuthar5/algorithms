"""
leetcode challenge: https://leetcode.com/problems/01-matrix/

Note: better solution is to make 2 passes through the matrix (left to right top to bottom & right to left bottom to top) 
however I wanted to practice implementing a BFS
"""

def bfs(matrix,i,j):
    queue=[(i-1,j,1), (i,j-1,1),(i,j+1,1), (i+1,j,1)]
    while True:
        node=queue.pop(0)
        if node[0] >=0 and node[0] < len(matrix) and node[1] >= 0 and node[1] < len(matrix[node[0]]):
            if matrix[node[0]][node[1]]==0:
                return node[2]
            else:
                queue.append((node[0]-1,node[1],node[2]+1))
                queue.append((node[0],node[1]-1,node[2]+1))
                queue.append((node[0],node[1]+1,node[2]+1))
                queue.append((node[0]+1,node[1],node[2]+1))

        
def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                matrix[i][j] = self.bfs(matrix,i,j)
    return matrix
