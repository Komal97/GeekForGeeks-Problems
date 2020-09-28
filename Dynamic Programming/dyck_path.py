'''
https://practice.geeksforgeeks.org/problems/dyck-path1028/1
Consider a N x N grid with indexes of top left corner as (0, 0). Dyck path is a staircase walk from bottom left, i.e., (N-1, 0) to top right, i.e., (0, N-1) that lies above the diagonal cells (or cells on line from bottom left to top right).
The task is to count the number of Dyck Paths from (N-1, 0) to (0, N-1).

Example 1:
Input:
N = 4
Output:
14 

Example 1:
Input:
N = 3
Output:
5
'''

# find catalan(N)
class Solution:
    def dyckPaths(self, N):
        if N == 0 or N == 1:
            return N
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, N+1):
            for j in range(i):
                dp[i] += (dp[j]*dp[i-j-1])
        return dp[N]
