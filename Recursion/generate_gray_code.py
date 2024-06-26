'''
https://practice.geeksforgeeks.org/problems/generate-grey-code-sequences/1
Given a number N, your task is to complete the function which generates all n-bit grey code sequences, a grey code sequence is a sequence such that successive patterns in it differ by one bit.
Example 1:
Input:
N = 2
Output: 00 01 11 10
Explanation: All 2-bit gray codes are
00, 01, 11, 10 such that successive
patterns in it differ by one bit.
Example 2:

Input:
N = 1
Output: 0 1
'''

# recursive
def generateCode(n):
    if n == 1:
       return ['0', '1']
    
    tempres = generateCode(n-1)
    myres = []
    for i in range(len(tempres)):
        myres.append('0' + tempres[i])                          # append 0 at n-1 numbers
        
    for i in range(len(tempres)-1, -1, -1):                 
        myres.append('1' + tempres[i])                          # append 1 at n-1 numbers in reverse order
        
    return myres

# iterative
def generateCode(n):
    
    res = ['0', '1']
    l = 0
    while l<n-1:
        j = len(res)-1                              # consider 0 and 1
        while j >= 0:   
            res.append('1' + res[j])                # append 1 to them in reverse order 0, 1, 11, 10
            res[j] = '0' + res[j]                   # simultaneously append 0 to existing 00, 01, 11, 10
            j -= 1
        l += 1
    
    return res