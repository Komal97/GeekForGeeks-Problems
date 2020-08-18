'''
https://practice.geeksforgeeks.org/problems/find-optimum-operation/0/
You are given a number N. You have to find the number of operations required to reach N from 0. You have 2 operations available:
Double the number
Add one to the number
Input:
2
8
7
Input:
4
5
Explanation:
Testcase1:
Input  : N = 8
Output : 4
0 + 1 = 1, 1 + 1 = 2, 2 * 2 = 4, 4 * 2 = 8
Testcase2:
Input  : N = 7
Output : 5
0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7
'''

# create dp of n+1 with dp[n] = 1
# at each place, put min(2*i and i+1) + 1
def minOperations(n):
       
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        val1 = dp[i*2] if i*2 <= n else float('inf')
        val2 = dp[i+1] if i+1 <= n else float('inf')
        dp[i] = min(val1, val2) + 1
    
    return dp[1]
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ans = minOperations(n)
        print(ans)
        t -= 1