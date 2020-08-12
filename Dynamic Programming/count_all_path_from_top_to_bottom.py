'''
https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right/0
The task is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.
Input:
1
3 3
Output:
6
'''

# smallest problem is at mxn
# at each point down_val + right_val is current value
M = 1000000007
def countPath(i, j, m, n):
    
    if i == m-1 and j == n-1:
        return 1
    
    val1 = 0
    val2 = 0
    if j+1 < n:
        val1 = countPath(i, j+1, m, n)
    if i+1 < m:
        val2 = countPath(i+1, j, m, n)
        
    return (val1 + val2)%M

M = 1000000007
def countPath(m, n):

    dp = [[0]*n for _ in range(m)]
    
    dp[m-1][n-1] = 1
    
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                continue
            else: 
                val1 = dp[i+1][j] if i+1 < m else 0
                val2 = dp[i][j+1] if j+1 < n else 0
                dp[i][j] = (val1 + val2)%M
                
    return dp[0][0]        
    
    
if __name__ == '__main__':
    t = int(input())
    while t:
        m, n = list(map(int, input().split()))
        print(countPath(0, 0, m, n))
        t -= 1