'''
https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1
You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, if yes, 
(s)he doesn’t know anyone in the party. Your task is to find the stranger (celebrity) in party.
You will be given a square matrix M[][] where if an element of row i and column j  is set to 1 it means ith person knows jth person.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Input :
2
3
0 1 0 0 0 0 0 1 0
2
0 1 1 0
Output :
1
-1

Explanation :
Testcase 1:
For the above test case the matrix will look like
0 1 0 
0 0 0
0 1 0
Here,  the celebrity is the person with index 1 ie id 1
'''
# method - 1, O(n^2)
# find row with all 0, and check if only row with zero then return that row number
# else if more than one rows or no row then -1 (mentioned in condition provided)
def getId(m,n): # m is 2-D matrix
    count = 0
    pos = -1
    for i in range(n):
        j = 0
        while(j<n):
            if m[i][j] == 1:
                break
            j += 1
        if j == n:
            pos = i
            count += 1
            
    return pos if count == 1 else -1

# method -2, O(n)
def getId(m,n):
    
    stack = []
    # push all candidates in stack
    for i in range(n):
        stack.append(i)
    
    while len(stack) >= 2:
        i = stack.pop()
        j = stack.pop()
        if m[i][j] == 1:
            # means i knows j -> i can't be celebrity
            stack.append(j)
        else:
            # means i doesn't know j -> j can't be celebrity
            stack.append(i)
            
    # at last, we have 1 potential candidate left in stack
    potential = stack.pop()
    # check potential candidate's column and row
    for i in range(n):
        if i!=potential:
            if m[i][potential] == 0 or m[potential][i] == 1:
                return -1
            
    return potential

