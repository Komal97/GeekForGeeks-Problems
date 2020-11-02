'''
https://www.geeksforgeeks.org/count-number-subarrays-given-xor/
Given an array of integers A and an integer B.
Find the total number of subarrays having bitwise XOR of all elements equals to B.
Input 1:
A = [4, 2, 2, 6, 4]
B = 6
Output:
4

Input 2:
A = [5, 6, 7, 8, 9]
B = 5
Output:
2

Explanation 1:
The subarrays having XOR of their elements as 6 are:
[4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
Explanation 2:
The subarrays having XOR of their elements as 2 are [5] and [5, 6, 7, 8, 9]
'''

from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        n = len(A)
        h = defaultdict(int)
        xor, count = 0, 0

        for i in range(n):
            xor ^= A[i]
            if xor == B:
                count += 1
            if xor^B in h:
                count += h[xor^B]
            h[xor] += 1
        
        return count
            
        