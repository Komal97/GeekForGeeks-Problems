'''
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
Consider a rat placed at (0, 0) in a square matrix of order N*N. It has to reach the destination at (n-1, n-1). 
Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). 
Value 0 at a cell in the matrix represents that it is blocked and cannot be crossed while value 1 at a cell in the matrix represents that it can be travelled through.
Expected Time Complexity: O((N2)4).
Expected Auxiliary Space: O(L*X), L = length of the path, X = number of paths.
Input:
3
4
1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1
4
1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1
2
1 0 1 0 

Output:
DRDDRR
DDRDRR DRDDRR
-1
'''

# if row or col goes out of bound or arr[r][c] = -1(visited) or arr[r][c] = 0(blocked), then base cond hit so return
# if we reach at bottom right corner, then print path and return
# else change arr[i][j] = -1(visited) and call in all 4 directions
# after processing all 4 directions, make arr[i][j] = 1 again so that same cell can be used by other path
def ratMaze(arr, i, j, path, ans):
    if i < 0 or j < 0 or i >= len(arr) or j >= len(arr) or arr[i][j] <= 0:
        return
    
    if i == len(arr)-1 and j == len(arr)-1:
        ans.append(path)
        return
    
    arr[i][j] = -1
    ratMaze(arr, i-1, j, path + 'U', ans)
    ratMaze(arr, i+1, j, path + 'D', ans)
    ratMaze(arr, i, j-1, path + 'L', ans)
    ratMaze(arr, i, j+1, path + 'R', ans)
    arr[i][j] = 1
    
def findPath(arr, n):
    
    ans = []
    ratMaze(arr, 0, 0, '', ans)
    return ' '.join(sorted(ans))