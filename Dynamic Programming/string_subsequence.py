'''
https://practice.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence/0
Given two strings S1 and S2, find the number of times the second string occurs in the first string, whether continuous or discontinuous.

Example 1:
Input: 
S1 = geeksforgeeks
S2 = gks
Output: 4
Explaination: For the first 'g' there are 3 ways and for the second 'g' there is one way. Total 4 ways.
'''

def countWays(self, S1, S2):
        
        n, m = len(S1), len(S2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        
        def count(s1, i, s2, j):
            if j == m:                                      # if patterm finish, 1 string found
                return 1
            elif j < m and i == n:                          # if string finish but pattern doesn't so no string 
                return 0
                
            if dp[i][j] != -1:
                return dp[i][j]
                
            val1 = 0
            val2 = 0
            
            # if char equal 
            # 2 cases => include current character or leave from string -> i++, j++ and i++, j
            # if char not equal then exclude current character from string -> i++, j
            if s1[i] == s2[j]:
                val1 = count(s1, i+1, s2, j+1)
            val2 = count(s1, i+1, s2, j)
            
            dp[i][j] = val1+val2
            return dp[i][j] 
            
        return count(S1, 0, S2, 0)