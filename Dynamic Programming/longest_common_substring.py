'''
https://practice.geeksforgeeks.org/problems/longest-common-substring/0
Given two strings X and Y. The task is to find the length of the longest common substring.
Input:
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Output:
4
1

Example:
Testcase 1: CDGH is the longest substring present in both of the strings.
'''

# if string match then dp[i][j] = 1 + dp[i-1][j-1] and keep maxlength
# if string doesn't match, don't do anything
def longest_common_substring(str1, str2, l1, l2):
    
    dp = [[0]*(l2+1) for _ in range(l1+1)]
    
    length = 0
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] 
                length = max(length, dp[i][j])
                
    return length

if __name__ == '__main__':
    t = int(input())
    while t:
        l1, l2 = list(map(int, input().split()))
        str1 = input()
        str2 = input()
        memo = [[-1]*(l2) for _ in range(l1)]
        print(longest_common_substring(str1, str2, l1, l2))
        t -= 1