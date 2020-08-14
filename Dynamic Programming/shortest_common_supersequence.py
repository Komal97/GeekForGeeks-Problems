'''
https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.
Note: str1 and str2 can have both uppercase and lowercase letters.
Input:
2
abcd xycd
efgh jghi
Output:
6
6
Explanation:
Test Case 1: One of the shortest answer can be abxycd, which is of length 6.
'''

# pattern is combine both strings and remove LCS part
# to solve - find LCS length
# ans = length of str1 + length of str2 - LCS length
def shortest_common_supersequence(str1, str2):
    
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0]*(l2+1) for _ in range(l1+1)]
    
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
    scs = l1 + l2 - dp[l1][l2]
    print(scs)
    
    # to print -> before moving in any direction, store current character
    output = ['']*scs

    i = l1 
    j = l2 
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            output[scs-1] = str1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                output[scs-1] = str1[i-1]       # before moving up store current
                i -= 1
            else:
                output[scs-1] = str2[j-1]       # before moving left store current
                j -= 1
        scs -= 1
        
    while i > 0:                                # if str1 has characters and str2 is empty
        output[scs-1] = str1[i-1]
        i -= 1
        scs -= 1
    while j > 0:                                # if str2 is empty and str2 has characters
        output[scs-1] = str2[j-1]
        j -= 1
        scs -= 1

    print(''.join(output))
    
    
if __name__ == '__main__':
    t = int(input())
    while t:
        str1, str2 = input().split()
        shortest_common_supersequence(str1, str2)
        t -= 1