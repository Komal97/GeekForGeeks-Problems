'''
https://practice.geeksforgeeks.org/problems/rod-cutting/0
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
Same piece can be consider again. Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
Input:
1
8
1 5 8 9 10 17 17 20
Output:
22
'''

# logic same as that of unbounded knapsack
# memoization
def rodCutting(price, n, memo):
    
    if n <= 0:                                              # call on max cut
        return 0
    
    if memo[n] != -1:
        return memo[n]
        
    maxval = 0
    for i in range(1, n+1):                                 # cut from 1 to n, for each n
        maxval = max(maxval, price[i-1] + rodCutting(price, n-i, memo)) 
    
    memo[n] = maxval
    return maxval

def rodCutting(price, n):
    
    dp = [-1]*(n+1)
    dp[0] = 0
    
    for cut in range(1, n+1):                               # denotes max cut (N)
        maxval = 0  
        for i in range(1, n+1):                             # denotes array price (price array) as well as cut (length array)
            if i<=cut :
                maxval = max(maxval, price[i-1] + dp[cut-i])
        dp[cut] = maxval
    
    return dp[n]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        price = list(map(int, input().split()))
        memo = [-1]*(n+1)
        print(rodCutting(price, n, memo))
        t -= 1
