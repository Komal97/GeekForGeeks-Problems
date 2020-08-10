'''
https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.
Input:
2
4
1 5 11 5
3
1 3 5 

Output:
YES
NO

Explanation:
Testcase 1: There exists two subsets such that {1, 5, 5} and {11}.
'''

# variation of target sum subsets (0-1 knapsack)
# if sum is odd, it can never partition into 2 subsets
# if sum if even, it can be partition, call targetSumSubet with sum/2 to check availability of one partiion
# if one partition is available, then second must be there
def equalPartition(arr, n, summ):
    
    dp = [[False]*(summ+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][summ]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        summ = sum(arr)
        if summ&1:                                          # if sum is odd, it can never partition into 2 subsets
            print('NO')
        else:
            ans = equalPartition(arr, n, summ//2)           # if sum if even, it can be partition
            if ans:                                         
                print('YES')
            else:
                print('NO')
        t -= 1