'''
https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC
Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS of "ABC" and "AC" is "AC" of length 2
'''
# memoization
def lenOfLCS(str1, l1, str2, l2, memo):
    
    if l1 == len(str1) or l2 == len(str2):
        return 0
    
    if memo[l1][l2] != -1:
        return memo[l1][l2]
    
    count = 0
    
    # if character match, then increment both pointers
    if str1[l1] == str2[l2]:
        count = 1 + lenOfLCS(str1, l1 + 1, str2, l2 + 1, memo)
    # if character doesn't match, then 2 choices - increment first string ptr and leave second as it is and same for sec ptr
    # return max of both choices
    else:
        choice1 = lenOfLCS(str1, l1, str2, l2 + 1, memo)
        choice2 = lenOfLCS(str1, l1 + 1, str2, l2, memo)
        count = max(choice1, choice2)
        
    memo[l1][l2] = count
    return count

# tabulation
def lenOfLCS(str1, str2, l1, l2):
    
    dp = [[0]*(l2+1) for _ in range(l1+1)]
    
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[l1][l2]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        l1, l2 = list(map(int, input().split()))
        str1 = input()
        str2 = input()
        memo = [[-1]*(l2) for _ in range(l1)]
        print(lenOfLCS(str1, 0, str2, 0, memo))
        t -= 1