'''
https://practice.geeksforgeeks.org/problems/convert-to-strictly-increasing-array/0
Given an array nums[] of N positive integers. Find the minimum number of operations required to modify the array such that array elements are in strictly increasing order (A[i] < A[i+1]).
Changing a number to greater or lesser than original number is counted as one operation.

Example 1:
Input: nums[] = [1, 2, 3, 6, 5, 4]
Output: 2
Explanation: By decreasing 6 by 2 and increasing 4 by 2, arr will be like [1, 2, 3, 4, 5, 6] which is stricly increasing.

Example 2:
Input: nums[] = [1, 2, 3, 4]
Output: 0
Explanation: Arrays is already strictly increasing.
'''

# find longest increasing subsequence with an extra cond
# check nums[j] <= nums[i] and (nums[i] - nums[j] >= i-j) 
# if a number is smaller than current then there should be enough numbers which can be accomodate b/w i and j
class Solution:
    def min_operations(self,nums):
    maxlis = 0
    n = len(nums)
    
    if n==1:
        return 0
        
    lis = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] <= nums[i] and (nums[i] - nums[j] >= i-j):
                lis[i] = max(lis[i], lis[j]+1)
        maxlis = max(maxlis, lis[i])
    
    return n-maxlis