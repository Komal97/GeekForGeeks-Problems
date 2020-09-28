'''
https://practice.geeksforgeeks.org/problems/handshakes1303/1
We have N persons sitting on a round table. Any person can do a handshake with any other person.
     1
2         3
     4
Handshake with 2-3 and 1-4 will cause cross.
In how many ways these N people can make handshakes so that no two handshakes cross each other. N would be even. 
'''
# given - 2*n
# ans = catalan(n)
# catalan(n) => if n=4, C0*C3 + C1*C2 + C2*C1 + C3*C0
class Solution:
    def count(self, N):
        
        n = N//2
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += (dp[j]*dp[i-j-1])

        return dp[n]