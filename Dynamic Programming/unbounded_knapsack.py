'''
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items/0
Given weights and values related to n items and the maximum capacity allowed for these items. 
What is the maximum value we can achieve if we can pick any weights any number of times for a total allowed weight of W?
Input:
2
2 3
1 1
2 1 
4 8
1 4 5 7
1 3 4 5
Output:
3
11
'''

# using 2-D DP
def unboundedKnapsack(price, weight, n, W):
    
    dp = [[0]*(W+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i][j-weight[i-1]])   # use current element again or not
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][W])

# using 1-D DP
def unboundedKnapsack(price, weight, n, W):
    
    dp = [0]*(W+1)                                              # dp of capacity
    
    for bagCap in range(1, W+1):
        max_profit = 0  
        for i in range(n):            
            # if current weight is consider then profit is current price + price of (capacity - current weight)                          
            if weight[i] <= bagCap:     
                remCap = bagCap - weight[i]                    
                totalVal = price[i] + dp[remCap]
                max_profit = max(max_profit, totalVal)          # find max value for current capacity
        dp[bagCap] = max_profit
        
    print(dp[W])
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, W = list(map(int, input().split()))
        price = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        unboundedKnapsack(price, weight, n, W)
        t -= 1