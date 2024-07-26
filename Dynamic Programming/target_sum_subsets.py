'''
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Input: 
arr[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: 
True  
There is a subset (4, 5) with sum 9.

Input: 
arr[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: 
False
There is no subset that add up to 30.
'''

# recursion 
def subsets(arr, idx, summ, out):
    if summ == 0:
        print(out)
        return
    if idx == len(arr):
        return
    

    val = arr[idx]
    subsets(arr, idx+1, summ, out)
    if summ - val >= 0:
        subsets(arr, idx+1, summ - val, out + [val])


arr = [10, 20, 30, 40, 50]
subsets(arr, 0, 60, [])

# variation of 0-1 knapsack
# recursion + memoization
def printIsSubsetPresent(arr, i, n, summ, dp):
    if summ == 0:
        return True
    if i == n and summ != 0:
        return False
    
    if dp[i][summ] != -1:
        return True if dp[i][summ] == 1 else False

    val1 = False
    if arr[i] <= summ:
        val1 = printIsSubsetPresent(arr, i+1, n, summ-arr[i], dp)
    val2 = printIsSubsetPresent(arr, i+1, n, summ, dp)

    if val1 or val2:
        dp[i][summ] = 1
    else:
        dp[i][summ] = 0
    return val1 or val2


# tabulation
def printIsSubsetPresentDp(arr, n, summ):
    
    dp = [[False]*(summ+1) for _ in range(n+1)]

    # if summ is given and n = 0, then no subset
    for i in range(summ+1):
        dp[0][i] = False
        
    # if summ = 0, then empty array is always there as subset
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, summ+1):
            # if current element is less than given sum
            if arr[i-1] <= j:
                # include current element or exclude current element in subset
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                # exclude current element in subset
                dp[i][j] = dp[i-1][j]
  
    return dp[n][summ]

arr = [2, 3, 7, 8, 10]
n = len(arr)
summ = 3
dp = [[-1]*(summ+1) for _ in range(n)]
ans1 = printIsSubsetPresent(arr, 0, n, summ, dp)
ans2 = printIsSubsetPresentDp(arr, n, summ)
print(ans1, ans2)