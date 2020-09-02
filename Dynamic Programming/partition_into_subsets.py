'''
https://www.geeksforgeeks.org/count-number-of-ways-to-partition-a-set-into-k-subsets/
You are given a number n, representing the number of elements.
You are given a number k, representing the number of subsets.
You are required to print the number of ways in which these elements can be partitioned in k non-empty subsets.
E.g.
For n = 4 and k = 3 total ways is 6
12-3-4
1-23-4
13-2-4
14-2-3
1-24-3
1-2-34

Input:
4
3
Output:
6
'''
#     1 2 3 [3]
# 12[3]          1 2[2]         n-1 members form team of k-1 and nth member in kth team -> 1 way * (n-1, k-1)
# n-1 members for team of k and nth attaches with all of them (k)   -> k ways *(n-1, k)
# recurrence => (k*partition(n-1, k)) + partition(n-1, k-1)
def partition(n, k, memo):
    
    if n <= 0 or k <= 0 or n < k:
        return 0
    elif n == k or k == 1:
        return 1
    
    if memo[n][k] != -1:
        return memo[n][k]
    
    memo[n][k] = (k*partition(n-1, k, memo)) + partition(n-1, k-1, memo)
    return memo[n][k]

# tabulation
def partition(n, k):
       
    dp = [[0]*(k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i < j:
                dp[i][j] = 0
            elif i == j or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (j*dp[i-1][j]) + dp[i-1][j-1]

    return dp[n][k]

n = int(input())
k = int(input())
memo = [[-1]*(k+1) for _ in range(n+1)]
ans = partition(n, k, memo)
print(ans)