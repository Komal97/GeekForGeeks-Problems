'''
https://www.geeksforgeeks.org/number-of-ways-to-reach-nth-floor-by-taking-at-most-k-leaps/
Given N number of stairs. Also given the number of steps that one can cover at most in one leap (K). 
The task is to find the number of possible ways one (only consider combinations) can climb to the top of the building in K leaps or less from the ground floor.
Input: 
N = 5, K = 3
Output: 5

Explanation:
To reach stair no-5 we can choose following combination of leaps:
1 1 1 1 1
1 1 1 2
1 2 2
1 1 3
2 3
'''


def findWays(n, k, output):
    if n == 0:
        print(output)
        return 1
    elif n < 0:
        return 0

    jumps = 0
    for i in range(1, k+1):
        jumps += findWays(n-i, k, output + str(i))
    return jumps

ans = findWays(5, 3, '')
print(ans)