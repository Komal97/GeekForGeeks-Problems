'''
https://practice.geeksforgeeks.org/problems/coin-change/0
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins.
The order of coins doesn’t matter. 
Input:
2
3
1 2 3
4
4
2 5 3 6
10

Output:
4
5

Explanation:
Testcase 1: The possiblities are as such: {1, 1, 1, 1}, {1, 1, 2}, {1, 3}, {2, 2}.
'''

# 2-D dp is same as that of combo of unbounded knapsack and count subsets
# memoized
def coinChange(arr, i, n, summ, memo):
    
    if summ == 0:
        return 1
    if i == n and summ != 0:
        return 0
    
    if memo[i][summ] != -1:
        return memo[i][summ]
        
    val1 = 0
    if arr[i] <= summ:
        val1 = coinChange(arr, i, n, summ-arr[i], memo)
    val2 = coinChange(arr, i+1, n, summ, memo)
    
    memo[i][summ] = val1 + val2
    return memo[i][summ]

# tabulation - using 2D dp
def coinChange(coins, n, summ):
    
    dp = [[0]*(summ+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
        
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][summ]
  
# using 1D dp
def coinChange(coins, n, summ):
    
    dp = [0]*(summ+1)
    dp[0] = 1
    
    for i in range(n):                                  # for each coins
        for j in range(coins[i], summ+1):               # check for each sum value 
            dp[j] += dp[j-coins[i]]
       
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        summ = int(input())
        memo = [[-1]*(summ+1) for _ in range(n)]
        print(coinChange(arr, 0, n, summ, memo))
        t -= 1
        
        