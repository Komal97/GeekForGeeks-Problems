'''
https://www.geeksforgeeks.org/minimum-xor-value-pair/
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Example:
Input 1: 
A = [0, 2, 5, 7]
Output: 2
Explanation:0 xor 2 = 2

Input 2:
A = [0, 4, 7, 9]
Output: 3
'''

# min xor is possible of 2 consecutive elements only in sorted array
class Solution:
    def findMinXor(self, A):
        
        n = len(A)
        A.sort()
        
        ans = float('inf')
        
        for i in range(n-1):
            xor = A[i] ^ A[i+1]
            ans = min(ans, xor)
        
        return ans