'''
https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/
Given two equally sized 1-D arrays A, B containing N integers each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum C valid sum combinations from all the possible sum combinations.
Input 1:
A = [3, 2]
B = [1, 4]
C = 2
Output: [7, 6]
 
Input 2:
A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4
Output: [10, 9, 9, 8]

Explanation 2:
10   (A : 4) + (B : 6)
9   (A : 4) + (B : 5)
9   (A : 3) + (B : 6)
8   (A : 3) + (B : 5)
'''

# sort both array
# push sum of max values first in max heap
# pop from heap, push i+1, j and i, j+1 sum in max heap
# to avoid i+1, j and i, j+1 to push again, keep set of indexes
from heapq import heappush, heappop
class Solution:
    def solve(self, A, B, C):
        
        n = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        ans = []
        s = set()
        heap = []
        heappush(heap, [-(A[0] + B[0]), 0, 0])
        s.add((0, 0))
        
        for c in range(C):
            summ, i, j = heap[0]
            s.remove((i, j))
            ans.append(-summ)
            heappop(heap)
            
            
            if i + 1 < n and (i+1, j) not in s:
                s.add((i+1, j))
                heappush(heap, [-(A[i+1] + B[j]), i+1, j])
            
            if j + 1 < n and (i, j+1) not in s:
                s.add((i, j+1))
                heappush(heap, [-(A[i] + B[j+1]), i, j+1])
        
        return ans
            