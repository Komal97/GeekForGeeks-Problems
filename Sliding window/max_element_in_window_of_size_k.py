'''
https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90
'''
# space - O(n) + stack space
# find next greater element at each index
def nextGreaterElement(arr, n):
    stack = []
    ans = [0]*n
    
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = n
        else:
            ans[i] = stack[-1]
        stack.append(i)
    return ans
    
def find_max_in_window(arr, n, k):
    
    nge = nextGreaterElement(arr, n)
    j = 0
    # for each value
    for i in range(n-k+1):
        if j<i:
            j = i
        # move j until we are getting larger element in that window size
        while nge[j] < i+k:
            j = nge[j]
        print(arr[j], end = " ")
    
# method - 2 - O(k) space
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        
        if not nums:
            return []
        
        deq = deque()
        n = len(nums)
        ans = []
        
        for i in range(k):
            # pop smaller element from last as current element is greater for current window 
            # if current < last element means it is not max in current window but can be max in future windows
            while len(deq) > 0 and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        
        for i in range(k, n):
            ans.append(nums[deq[0]])
            
            # pop out of window elements
            while len(deq) > 0 and deq[0] <= i-k:
                deq.popleft()
            
            # pop smaller element from last as current element is greater for current window 
            # if current < last element means it is not max in current window but can be max in future windows
            while len(deq) > 0 and nums[i] >= nums[deq[-1]]:
                deq.pop()
             
            deq.append(i)
        
        ans.append(nums[deq[0]])
        return ans