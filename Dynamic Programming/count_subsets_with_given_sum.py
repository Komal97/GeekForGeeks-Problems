'''
https://practice.geeksforgeeks.org/problems/perfect-sum-problem/0
Given an array of integers and a sum, the task is to count all subsets of given array with sum equal to given sum.
Input:
2
6
2 3 5 6 8 10
10
5
1 2 3 4 5
10

Output:
3
3

Explanation:
Testcase 1: possible subsets : (2,3,5) , (2,8) and (10)
Testcase 2: possible subsets : (1,2,3,4) , (2,3,5) and (1,4,5)  
'''

# recursion
# variation of target sum subsets (0-1 knapsack)
# if include element, return sum1, 
# if exclude element, return sum2
# return sum1 + sum2
def countSubsets(arr, i, n, summ):
    
    if summ == 0:
        return 1
    
    if i== n and summ != 0:
        return 0
    
    val1 = 0
    if arr[i] <= summ:
        val1 = countSubsets(arr, i+1, n, summ-arr[i])
    val2 = countSubsets(arr, i+1, n, summ)
    
    return val1 + val2

# tabulation
M = 1000000007
def countSubsets(arr, n, summ):
    
    dp = [[0]*(summ+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
        
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]]) % M
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][summ]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        summ = int(input())
        print(countSubsets(arr, 0, n, summ))
        t -= 1
        