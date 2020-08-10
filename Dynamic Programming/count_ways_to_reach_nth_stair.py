'''
https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0
There are N stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does matter).
Input:
3
4
10
24
Output:
5
89
75025
'''

# memoization
M = 1000000007
def countWays(n, memo):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    if memo[n] > 0:
        return memo[n]
    
    summ = countWays(n-1, memo) + countWays(n-2, memo)
    memo[n] = summ % M
    return memo[n]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        memo = [0]*(n+1)
        print(countWays(n, memo))
        t -= 1
        
# tabulation method 
def countWays(n):
    
    dp = [0]*(n+1)
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%M
        
    print(dp[n])
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        countWays(n)
        t -= 1

        