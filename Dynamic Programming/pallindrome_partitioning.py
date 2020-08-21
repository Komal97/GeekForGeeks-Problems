'''
https://www.interviewbit.com/problems/palindrome-partitioning-ii/#
Given a string A, partition A such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of A.
Input 1:
A = "aba"
Output 1:
0
Explanation 1:
"aba" is already a palindrome, so no cuts are needed.

Input 2:
A = "aab"
Output 2:
1
Explanation 2:
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

# same as MCM
# check for each k, whether both sides of k is pallindrome
class Solution:
    
    def isPalindrome(self, string, i, j):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def partition(self, string, i, j, memo):
        # if empty string or size 1 string then no partition
        if i >= j:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        # if whole string is pallindrome then no partition
        if self.isPalindrome(string, i, j):
            return 0
        
        # check for each cut
        minans = float('inf')
        for k in range(i, j):
            left = 0
            right = 0
            if memo[i][k] != -1:
                left = memo[i][k]
            else:
                left = self.partition(string, i, k, memo)
                
            if memo[k+1][j] != -1:
                right = memo[k+1][j]
            else:
                right = self.partition(string, k+1, j, memo)
                
            temp = 1 + left + right
            minans = min(temp, minans)
            
        memo[i][j] = minans
        return minans
        
    def minCut(self, A):
    
        n = len(A)
        
        if n == 0 or n == 1:
            return 0
            
        memo = [[-1]*(n) for _ in range(n)]
        return self.partition(A, 0, n-1, memo)
        