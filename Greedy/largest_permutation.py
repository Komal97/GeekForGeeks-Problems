'''
https://www.geeksforgeeks.org/largest-permutation-k-swaps/?ref=rp
Given a permutation of first n natural numbers as array and an integer k. 
Print the lexicographically largest permutation after at most k swaps
Examples:

Input: A[] = {4, 5, 2, 1, 3}
       k = 3
Output: 5 4 3 2 1
Swap 1st and 2nd elements: 5 4 2 1 3 
Swap 3rd and 5th elements: 5 4 3 1 2 
Swap 4th and 5th elements: 5 4 3 2 1 

Input: A[] = {2, 1, 3}
       k = 1
Output: 3 1 2
Swap 1st and 3rd elements: 3 1 2 
'''

# The largest permutation is found when the largest elements are at the front of the array, 
# i.e. the largest elements are sorted in decreasing order
# now to find position to swap, first store elements in map 
# check arr[i] == n-i, then continue else find position of n-i element from map and then swap elements
class Solution:
    def solve(self, A, k):
        
        n = len(A)
        
        pos = {}
        
        for i, num in enumerate(A):
            pos[num] = i
        
        for i in range(n):
            if k == 0:
                break
            
            if A[i] == n-i:
                continue
            
            # find position of element to be swapped with
            # swap indexes in map
            idx = pos[n-i]
            pos[n-i] = i
            pos[A[i]] = idx
            
            # then swap elements
            A[i], A[idx] = A[idx], A[i]
            
            k -= 1
        
        return A
            
            
            