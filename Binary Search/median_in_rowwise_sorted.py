'''
https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.
Example 1:
Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5
Explanation:
Sorting matrix elements gives us {1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
'''

# method - 1 - using heap but take extra space	- O(col * log(row))
# find kth (total / 2) element in matrix
from heapq import heappush, heappop
class Solution:
    
    def findMedian(self, A):
        
        n, m = len(A), len(A[0])
        
        def findElement(k):

            heap = []
            for i in range(n):
                heappush(heap, [A[i][0], i, 0])
           
            element = -1
            for i in range(k):
                element, s, e = heap[0]
                heappop(heap)
                if e + 1 < m:
                    heappush(heap, [A[s][e+1], s, e+1])
                    
            return element
        
        totalelements = n * m
        k = totalelements//2
        if totalelements & 1:
            return findElement(k+1)
        return (findElement(k) + findElement(k+1))/2

# method - 2 - using binary search - O(32 * row * log(col))
from bisect import bisect_right
class Solution:
   
    def findMedian(self, A):
        
        n, m = len(A), len(A[0])
        
        mi = A[0][0]
        mx = 0
        
        for i in range(n):
            mi = min(mi, A[i][0]) 
            mx = max(mx, A[i][m-1])
        
        total = (n*m+1)//2
        while mi < mx:
            mid = mi + (mx - mi)//2
            place = 0
            
            for i in range(n):
                j = bisect_right(A[i], mid)
                place += j
            if place < total:
                mi = mid + 1
            else:
                mx = mid
        return mi
       