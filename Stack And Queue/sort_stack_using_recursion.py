'''
https://practice.geeksforgeeks.org/problems/sort-a-stack/1
Given a stack, the task is to sort it such that the top of the stack has the greatest element.
Expected Time Complexity : O(N*N)
Expected Auixilliary Space : O(N) recursive.
Input:
2
3
3 2 1
5
11 2 32 3 41

Output:
3 2 1
41 32 11 3 2
'''

def insertAtPos(s, x):
    if len(s) == 0 or s[-1]>x:
        s.append(x)
        return
    
    y = s.pop()
    insertAtPos(s, x)
    s.append(y)
    
def sorted(s):
    if len(s) == 0:
        return 
    
    x = s.pop()
    sorted(s)
    insertAtPos(s, x)