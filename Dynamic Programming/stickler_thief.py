'''
https://practice.geeksforgeeks.org/problems/stickler-theif/0
Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. 
According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what 
amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. 
Each house has a[i] amount of money present in it.
Input:
2
6
5 5 10 100 10 5
3
1 2 3
Output:
110
4

Explanation:
Testcase1:
5+100+5=110
Testcase2:
1+3=4
'''

# recursive
def find_max_loot(arr, i, n):
    if i>= n:
        return 0
    
    val1 = arr[i] + find_max_loot(arr, i+2, n)              # loot i and call on i+2
    val2 = find_max_loot(arr, i+1, n)                       # leave i and call on i+1
    
    return max(val1, val2)                                  # return max of both strategies

# tabulation using 1-D
def find_max_loot(arr, n):
    
    dp = [0]*(n+1)
    for i in range(n-1, -1, -1):
        val1 = dp[i+2] if i+2<n else 0
        val2 = dp[i+1] if i+1<n else 0
        dp[i] = max(arr[i] + val1, val2)
    return dp[0]

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        ans = find_max_loot(arr, 0, n)
        print(ans)
        t -= 1