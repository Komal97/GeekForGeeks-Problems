'''
https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/
Given an array of integers. Write a program to find the K-th largest sum of contiguous subarray within the array of numbers which has negative and positive numbers.
Examples:
Input: 
a[] = {20, -5, -1} 
k = 3
Output: 14
Explanation: All sum of contiguous subarrays are (20, 15, 14, -5, -6, -1) 
so the 3rd largest sum is 14.

Input: 
a[] = {10, -10, 20, -40} 
k = 6
Output: -10 
Explanation: The 6th largest sum among sum of all contiguous subarrays is -10.
'''

# we cannot store summ of all subarrays as number of subarrays can be large which cannot fit in memory
# so use variable sum += arr[j] where i <= j < n
# use heap to find kth largest sum
# O(n^2 log k)
from heapq import heappush, heapreplace
def kth_largest_sum(arr, n, k):
 
    heap = []
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if len(heap) < k:
                heappush(heap, summ)
            elif heap[0] < summ:
                heapreplace(heap, summ)
    
    print(heap[0])

arr = [10, -10, 20, -40]
k = 6

kth_largest_sum(arr, len(arr), k)