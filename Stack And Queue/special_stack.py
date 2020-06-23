'''
https://practice.geeksforgeeks.org/problems/special-stack/1
Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.
Expected Time Complexity: O(1) for all the 5 functions.
Expected Auxiliary Space: O(1) for all the 5 functions.
Input:
1
5
18 19 29 15 16
Output:
15
'''
# method - 1, create auxilliary stack with minimum element till now and always return top of stack
# O(1) time & O(n) space
min_stack = []
def push(arr, ele):
    global min_stack
    arr.append(ele)
    x = min(min_stack[-1], ele) if len(min_stack)>0 else ele
    min_stack.append(x)

def pop(arr):
    if isEmpty(arr):
        return
    global min_stack
    arr.pop()
    min_stack.pop()

def isFull(n, arr):
    return len(arr) == n

def isEmpty(arr):
    return len(arr) == 0

def getMin(n, arr):
    global min_stack
    return min_stack[-1] if not isEmpty(arr) else -1