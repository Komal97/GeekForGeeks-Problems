'''
https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/0
Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
Input:
2
3
abc
5
axxxy

Output:
0
2
'''

# define str2 = str1
# find LCS based on condition str1[i-1] == str2[j-1] and i-1 != j-1
# this is because repeating characters are at different positions
def longest_repeating_subsequence(str1, l1):
    
    str2 = str1
    
    dp = [[0]*(l1+1) for _ in range(l1+1)]
    
    for i in range(1, l1+1):
        for j in range(1, l1+1):
            if str1[i-1] == str2[j-1] and i-1 != j-1:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[l1][l1])

if __name__ == '__main__':
    t = int(input())
    while t:
        l1 = int(input())
        str1 = input()
        longest_repeating_subsequence(str1, l1)
        t -= 1
        