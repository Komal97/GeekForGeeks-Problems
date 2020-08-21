'''
https://practice.geeksforgeeks.org/problems/friends-pairing-problem/0
Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. 
Find out the total number of ways in which friends can remain single or can be paired up.
Examples:
Input  : n = 3
Output : 4
Explanation
{1}, {2}, {3} : all single
{1}, {2,3} : 2 and 3 paired but 1 is single.
{1,2}, {3} : 1 and 2 are paired but 3 is single.
{1,3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1,2} and {2,1} are considered same.
Input:
2
3
2
Output:
4
2
'''

# choose single, and call on i-1
# for pair - choose current and other from i-1 so nC1 and call on i-2
# dp[i] = (dp[i-1] + (i-1)*dp[i-2])
M = 1000000007
def pair_friends(n):
    
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + (i-1)*dp[i-2])%M                 
        
    return dp[n]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ans = pair_friends(n)
        print(ans)
        t -= 1