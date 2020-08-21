'''
https://practice.geeksforgeeks.org/problems/ways-to-tile-a-floor/0
Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, the task is to find the number of ways the floor can be tiled. 
A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile.
Input
2
5
3

Output
8
3
'''
# base conditions
# if length = 1, then only 1 option
# if length = 2, then 2 options either put both 1x2 or keep both 2x1
# at each positions, 2 choices are there - either put 2x1 so n-2 or 1x2 so n-1
# dp[i] = dp[i-1] + dp[i-2]
def ways_to_tile(n):
   
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ans = ways_to_tile(n)
        print(ans)
        t -= 1
        
     
'''
https://practice.geeksforgeeks.org/problems/count-the-number-of-ways-to-tile-the-floor-of-size-n-x-m-using-1-x-m-size-tiles/0
Given a floor of size n x m and tiles of size 1 x m. The problem is to count the number of ways to tile the given floor using 1 x m tiles. 
A tile can either be placed horizontally or vertically. Both n and m are positive integers and 2 < = m.
Input:
2
2 3
4 4
Output:
1
2
'''

# if n < m, then 1 way
# if n==m, then 2 ways
# else dp[i] = (dp[i-1] + dp[i-m])
M = 1000000007
def ways_to_tile(n, m):
    
    dp = [0]*(n+1)
    
    for i in range(1, n+1):
        if i < m:                                       
            dp[i] = 1
        elif i == m:
            dp[i] = 2
        else:
            dp[i] = (dp[i-1] + dp[i-m])%M

    return dp[n]

if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = list(map(int, input().split()))
        ans = ways_to_tile(n, m)
        print(ans)
        t -= 1