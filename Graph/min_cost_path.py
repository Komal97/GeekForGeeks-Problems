'''
https://practice.geeksforgeeks.org/problems/minimum-cost-path/0
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum. 
You can move in 4 directions : up, down, left an right.
Note : It is assumed that negative cost cycles do not exist in input matrix.
Input:
2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14

Output:
327
63
Explanation:
Testcase 1:
A cost grid is given in below diagram, minimum cost to reach bottom right from top left is 327 
(31 + 10 + 13 + 47 + 65 + 12 + 18 + 6 + 33 + 11 + 20 + 41 + 20)
'''

# using dijkstra algorithm -> neighbors are 4 directions -> up, down, right, left
# push [dist + mat[i][j], [i, j]] in heap
from heapq import heappush, heappop
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def min_cost_path(mat, n):
    
    visited = [[False]*n for _ in range(n)]
    heap = []
    heappush(heap, [mat[0][0], 0, 0])
    
    while len(heap) > 0:
        dist, row, col = heap[0]
        heappop(heap)
        
        if row == n-1 and col == n-1:
            return dist
            
        if visited[row][col]:
            continue
        
        visited[row][col] = True
        for k in range(len(dx)):
            nrow = row + dx[k]
            ncol = col + dy[k]
            if nrow>=0 and ncol>=0 and nrow<n and ncol<n and (not visited[nrow][ncol]):
                heappush(heap, [mat[nrow][ncol]+dist, nrow, ncol])

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    mat = []
    k = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(arr[k])
            k += 1
        mat.append(row)
    
    ans = min_cost_path(mat, n)
    print(ans)
    
    t -= 1