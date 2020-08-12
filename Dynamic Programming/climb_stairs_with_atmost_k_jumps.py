'''
https://www.geeksforgeeks.org/number-of-ways-to-reach-nth-floor-by-taking-at-most-k-leaps/
Given N number of stairs. Also given the number of steps that one can cover at most in one leap (K). 
The task is to find the number of possible ways one (only consider combinations) can climb to the top of the building in K leaps or less from the ground floor.
Input: 
N = 5, K = 3
Output: 
5
Explanation
To reach stair no-5 we can choose following combination of leaps:
1 1 1 1 1
1 1 1 2
1 2 2
1 1 3
2 3
Therefore the answer is 5.

Input: N = 29, K = 5
Output: 603
'''

# same as coin change 1 (combination)
def numberOfWays(n, k):
    
    dp = [0]*(n+1)
    dp[n] = 1 
    
    for leap in range(1, k+1):                              # for each leap
        for i in range(n-1, -1, -1):                        # check for each element
            if i + leap <= n:
                dp[i] += dp[i+leap]
    print(dp[0])

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        numberOfWays(n, k)
        t -= 1