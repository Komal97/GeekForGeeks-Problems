'''
https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
Given an array, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
Input:
2
4
1 6 5 11
4
36 7 46 40

Output : 
1
23

Explaination :
Testcase 1:
Subset1 = {1, 5, 6} ; sum of Subset1 = 12
Subset2 = {11} ;       sum of Subset2 = 11

Testcase 2:
Subset1 = {7, 46} ;   sum = 53
Subset2 = {36, 40} ; sum = 76
'''
# closest difference can be 0 which can be find out by sum-sum/2
# using given logic and knapsack trick, calculate sum of array then find sum(partition) in array closest to sum/2, 
# then part2 can be calculated using sum-part1 and ans will be abs(part1-part2)

# recursive
def minSumPartition(arr, n, i, summ):
    # if array finish or sum = 0 means we dont need to add anything so 0
    if i == n or summ == 0:     
        return 0
        
    val1 = 0
    
    # include current element to find sum
    if arr[i] <= summ:
        val1 = arr[i] + minSumPartition(arr, n, i+1, summ-arr[i])
    
    # exclude current element to find sum 
    val2 = minSumPartition(arr, n, i+1, summ)
    return max(val1, val2)

# tabulation
def minSumPartition(arr, n, summ):
       
    dp = [[0]*(summ+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1]] + arr[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][summ]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        summ = sum(arr)
        summ1 = minSumPartition(arr, n, summ//2)
        summ2 = summ-summ1
        print(abs(summ1-summ2))
        t -= 1