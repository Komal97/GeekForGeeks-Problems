'''
https://www.geeksforgeeks.org/maximum-profit-sale-wines/
Given n wines in a row, with integers denoting the cost of each wine respectively. Each year you can sale the first or the last wine in the row. 
However, the price of wines increases over time. Let the initial profits from the wines be P1, P2, P3…Pn. On the Yth year, 
the profit from the ith wine will be Y*Pi. Calculate the maximum profit from all the wines.
Input: Price of wines: 2 4 6 2 5
Output: 64
'''

# consider 2 choices and return max 
# 1) consider first bottle and find max from remaining
# 2) consider last bottle and find max from remaining
def wine_prob(arr, i, j, year, memo):
    if i > j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    val1 = (arr[i] * year) + wine_prob(arr, i+1, j, year+1, memo)
    val2 = (arr[j] * year) + wine_prob(arr, i, j-1, year+1, memo)
    
    memo[i][j] = max(val1, val2)
    return memo[i][j]

# tabulation
def wine_prob(arr, n):
    
    dp = [[0]*n for _ in range(n)]
    year = n
    for i in range(n):
        dp[i][i] = year*arr[i]
        
    year -= 1
    for length in range(2, n+1):
        start = 0
        end = n-length 
        while start <= end:
            endwindow = start + length - 1
            dp[start][endwindow] = max(arr[start]*year + dp[start+1][endwindow], arr[endwindow]*year + dp[start][endwindow-1])
            start += 1
        year -= 1

    return dp[0][n-1]

arr = [1, 4, 2, 3]
n = len(arr)
memo = [[-1]*(n) for _ in range(n)]
ans = wine_prob(arr, 0, n-1, 1, memo)
print(ans)