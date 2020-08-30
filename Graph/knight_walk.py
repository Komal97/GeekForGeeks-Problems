'''
https://practice.geeksforgeeks.org/problems/knight-walk/0
Given a chess board of order N x M and source points (s1, s2) and destination points (d1, d2). The task to find minimum number of moves required by the Knight to go to the destination cell.
Note: The chess board consists of rows numbered (1 to N) and columns (1 to M).
Input:
2
4 7
2 6 2 4
7 13
2 8 3 4

Output:
2
3

Explanation:
Testcase 1: One possible move for Knight is from 2, 6 to 4, 5 and then to 2, 4 which is our destination.]
'''

# method - 1 => recursion with backtracking
# method - 2 => using BFS
# neighbours are 8 moves where knight can go
# push [dist+1, [x, y]] in queue
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def minmoves(r, c, s1, s2, d1, d2):
    
    visited = [[False]*(c+1) for _ in range(r+1)]
   
    q = deque()
    q.append([0, [s1, s2]])
   
    while len(q) > 0:
        front = q.popleft()
        dist = front[0]
        i, j = front[1]
        
        if i == d1 and j == d2:
            return dist
            
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        
        for k in range(len(dx)):
            if i+dx[k] >0 and j+dy[k] > 0 and j+dy[k] <= c and i+dx[k] <= r:
                if not visited[i+dx[k]][j+dy[k]]:
                    q.append([dist+1, [i+dx[k], j+dy[k]]])
        
    return -1    
        
t = int(input())
while t:
    r, c = list(map(int, input().split()))
    s1, s2, d1, d2 = list(map(int, input().split()))
    
    ans = minmoves(r, c, s1, s2, d1, d2)
    print(ans)
    t -= 1