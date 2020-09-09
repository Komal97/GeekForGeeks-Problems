'''
https://practice.geeksforgeeks.org/problems/interleaved-strings/1
Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. 
C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.
Example 1:
Input:
A = YX, B = X, C = XXY
Output: 0
Explanation: XXY is not interleaving of YX and X
Example 2:

Input:
A = aab, B = axy, C = aaxaby
Output: 1
'''
# 3 cases => 1) if A[i] = C[j]
#            2) if B[i] = C[j]
#            3) if A[i] = C[k] and B[j] = C[k]
# if A[i] = C[k], inc i and k
# if B[j] = C[k], inc j and k
# return 'or' of both results
def checkInterleave(A, i, B, j, C, k, memo):
    
    if k == len(C):
        return 1
        
    if memo[i][j] != -1:
        return memo[i][j]
        
    check1 = 0
    check2 = 0
    
    if i < len(A) and A[i] == C[k]:
        check1 =  checkInterleave(A, i+1, B, j, C, k+1, memo)
    if j < len(B) and B[j] == C[k]:
        check2 = checkInterleave(A, i, B, j+1, C, k+1, memo)
        
    memo[i][j] = check1 or check2
    return memo[i][j]
    
def isInterleave(A, B, C):
    if len(C) != len(A) + len(B):
        return 0
    memo = [[-1]*(len(B)+1) for _ in range(len(A)+1)]
    return int(checkInterleave(A, 0, B, 0, C, 0, memo))