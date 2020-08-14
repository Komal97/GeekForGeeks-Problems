'''
https://www.geeksforgeeks.org/printing-longest-common-subsequence/
Given two sequences, print the longest subsequence present in both of them.
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
Input:
6 6
ABCDGH
AEDFHR
Output:
ADH
'''

def LCS(str1, l1, str2, l2):
    
    dp = [[0]*(l2+1) for _ in range(l1+1)]

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    print(dp[l1][l2])
    printLCS(str1, str2, l1, l2, dp)

# start from bottom right
# if character match, then decrement i-- and j--
# if not then, check if dp[i-1][j] > dp[i][j-1] then i-- else j--
# this is reverse of finding LCS
def printLCS(str1, str2, l1, l2, dp):

    length = dp[l1][l2]
    output = ['']*(length)
    
    i = l1
    j = l2
    while i > 0 and j > 0 and length >= 0:
        if str1[i-1] == str2[j-1]:
            output[length-1] = str1[i-1]
            i -= 1
            j -= 1
            length -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
    print(''.join(output))

if __name__ == '__main__':
   
    l1, l2 = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    LCS(str1, l1, str2, l2)
        