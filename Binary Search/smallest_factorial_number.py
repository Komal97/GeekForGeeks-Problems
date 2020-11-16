'''
https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1#
Given a number n. The task is to find the smallest number whose factorial contains at least n trailing zeroes.

Example 1:
Input:
n = 1
Output: 5
Explanation : 5! = 120 which has at least 1 trailing 0.

Example 2:
Input:
n = 6
Output: 25
Explanation : 25! has at least 6 trailing 0.

Expected Time Complexity: O(log2 N * log5 N).
Expected Auxiliary Space: O(1).
'''

# using binary search
# s = 1 & e = 5*n
# find mid and check trailing zeroes 
class Solution:
    def findNum(self, n : int):
        
        def countTrailingZeros(num):
            nonlocal n
            
            count = 0
            
            while num:
                count += (num//5)
                num //= 5
            return count
        
        if n == 0:
            return 1
        
        s = 1
        e = 5*n
        
        ans = -1
        while s <= e:
            mid = s + (e-s)//2
            if countTrailingZeros(mid) >= n:
                e = mid - 1
                ans = mid
            else:
                s = mid + 1
                
        return ans  