'''
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, 
find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
Input:
2
3
4
1 2 3
4 5 1
3
3
1 2 3
4 5 6
Output:
3
0
Explanation:
Test Case 1: 
With W = 4, you can either choose the 0th item or the 2nd item. Thus, the maximum value you can generate is the max of val[0] and val[2], which is equal to 3.
Test Case 2: 
With W = 3, there is no item you can choose from the given list as all the items have weight greater than W. Thus, the maximum value you can generate is 0.
'''

# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
# recursion
# if weight is considerable then take max(profit by included current item or excluding)
# if weight is not considerable then exclude current item
def maxProfit(price, weight, i, n, W):
    if i == n or W <= 0:
        return 0 
    
    val1 = 0
    if weight[i] <= W:
        val1 = price[i] + maxProfit(price, weight, i+1, n, W-weight[i])
 
    val2 = maxProfit(price, weight, i+1, n, W)
    
    return max(val1, val2)

# memoization
dp = [[0]*(1001) for _ in range(1001)]
def maxProfit(price, weight, i, n, W):
    global dp
    if i == n or W <= 0:
        return 0 
    
    if dp[i][W] != 0:
        return dp[i][W]
        
    val1 = 0
    if weight[i] <= W:
        val1 = price[i] + maxProfit(price, weight, i+1, n, W-weight[i])

    val2 = maxProfit(price, weight, i+1, n, W)
    ans =  max(val1, val2)
    
    dp[i][W] = ans
    return ans

# bottom-down (tabulation)
def maxProfit(price, weight, n, W):
    
    dp = [[0]*(W+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i-1] <= j:
                # dp[i-1][j] = if not included then take value which is given by previous items
                # dp[i-1][j-weight[i-1]] =  if included then take value which is given by previous items with W-current weight
                dp[i][j] = max(dp[i-1][j], price[i-1] + dp[i-1][j-weight[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
                
    print(dp[n][W])  
