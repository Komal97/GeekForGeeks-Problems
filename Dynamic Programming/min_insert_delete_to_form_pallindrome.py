'''
https://practice.geeksforgeeks.org/problems/minimum-deletitions/0
Given a string of S as input. Your task is to write a program to remove or delete minimum number of characters from the string so that the resultant string is palindrome.
Input:
2
aebcbda
geeksforgeeks
Output:
2
8
'''

# find LPS
# number of deletions = length - LPS
def min_delete(str1, l1):
    
    str2 = str1[::-1]
    
    dp = [[0]*(l1+1) for _ in range(l1+1)]
    
    for i in range(1, l1+1):
        for j in range(1, l1+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    ans = l1-dp[l1][l1]
    print(ans)

if __name__ == '__main__':
    t = int(input())
    while t:
        str1 = input()
        min_delete(str1, len(str1))
        t -= 1
        
        
'''
https://practice.geeksforgeeks.org/problems/form-a-palindrome/0
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
Input:
3
abcd
aba
geeks

Output:
3
0
3
'''

# find LPS
# if LPS = 0 then insertions = length-1
# if not then length-LPS (which is equal to number of deletion)
def min_insert(str1, n):
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    str2 = str1[::-1]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lps = dp[n][n]
    if lps == 0:
        print(n-1)
    else:
        print(n-lps)

if __name__ == '__main__':
    t = int(input())
    while t:
        str1 = input()
        min_insert(str1, len(str1))
        t -= 1