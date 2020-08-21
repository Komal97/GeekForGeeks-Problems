'''
https://practice.geeksforgeeks.org/problems/cutted-segments/0
Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a way that the cut length of a line segment each time is integer either x , y or z.
And after performing all cutting operation the total number of cutted segments must be maximum. 
Input
2
4
2 1 1
5
5 3 2
Output
4
2
In first test case, total length is 4, and cut lengths are 2, 1 and 1. 
We can make maximum 4 segments each of length 1. In secon test case, we can make two segments of lengths 3 and 2.
'''

# memoized
import sys
sys.setrecursionlimit(10000)
def maximize_cut(n, x, y, z, memo):
    
    if n == 0:
        return 0
        
    if memo[n] != -1:
        return memo[n]

    val1 = float('-inf')                                # use if input is invalid
    val2 = float('-inf')
    val3 = float('-inf')
    if n >= x:
        val1 = 1 + maximize_cut(n-x, x, y, z, memo)     # add only if returned value is valid
    if n >= y:
        val2 = 1 + maximize_cut(n-y, x, y, z, memo)
    if n >= z:
        val3 = 1 + maximize_cut(n-z, x, y, z, memo)

    memo[n] = max(val1, max(val2, val3))
    return memo[n]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        x, y, z = list(map(int, input().split()))
        memo = [-1]*(n+1)
        ans = maximize_cut(n, x, y, z, memo)
        print(ans)
        t -= 1
    
# tabulation
def maximize_cut(n, x, y, z):
    
    dp = [0]*(n+1)
    
    for i in range(1, n+1):  
        val1 = 1 + dp[i-x] if i>=x else float('-inf')
        val2 = 1 + dp[i-y] if i>=y else float('-inf')
        val3 = 1 + dp[i-z] if i>=z else float('-inf')
        dp[i] = max(val1, max(val2, val3))
        
    return dp[n]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        x, y, z = list(map(int, input().split()))
        ans = maximize_cut(n, x, y, z)
        print(ans)
        t -= 1