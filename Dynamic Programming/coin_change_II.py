'''
https://practice.geeksforgeeks.org/problems/number-of-coins/0/
Given a value V. You have to make change for V cents, given that you have infinite supply of each of C{ C1, C2, .. , Cm} valued coins. 
Find the minimum number of coins to make the change.
Output:
Print the minimum number of coins to make the change, if not possible print "-1".
Example:
Input:
1
7 2
2 1

Output:
4

Explanation :
Testcase 1: We can use coin with value 2 three times, and coin with value 1 one times to change a total of 7.
'''

# memoization
def coinChange(arr, i, n, summ, memo):
    
    if summ == 0:
        return 0
    
    if i == n and summ != 0:
        return float('inf')
    
    if memo[i][summ] != -1:
        return memo[i][summ]
        
    val1 = float('inf')
    if arr[i] <= summ:
        val1 = coinChange(arr, i, n, summ-arr[i], memo)
        if val1 != float('inf'):
            val1 += 1
    
    val2 = coinChange(arr, i+1, n, summ, memo)
    
    memo[i][summ] = min(val1, val2)
    return memo[i][summ]
    
# tabulation
def coinChange(arr, n, summ):
    
    dp = [[float('inf')]*(summ+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
        
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1] <= j:
                val1 = dp[i][j-arr[i-1]]
                if val1 != float('inf'):
                    val1 += 1
                val2 = dp[i-1][j]
                dp[i][j] = min(val1, val2)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][summ] 

if __name__ == '__main__':
    t = int(input())
    while t:
        summ, n = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        memo = [[-1]*(summ+1) for _ in range(n+1)]
        ans = coinChange(arr, 0, n, summ, memo)
        if ans == float('inf'):
            print(-1)
        else:
            print(ans)
        t -= 1