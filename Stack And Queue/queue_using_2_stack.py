'''
https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1
Implement a Queue using 2 stacks s1 and s2 .

Input:
The first line of the input contains an integer 'T' denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer Q denoting the number of queries . 
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)

Expected Time Complexity : O(1) for both push() and O(N) for pop().
Expected Auxilliary Space : O(N).
Input:
2
5
1 2 1 3 2 1 4 2
4
1 2 2 2 1 4
Output:
2 3
2 -1
'''
def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)

# iterative popping using 2 stacks
def transfer(s1, s2, n):
    for i in range(n):
        s2.append(s1.pop())

def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    n = len(stack1)
    
    if n==0:
        return -1
        
    transfer(stack1, stack2, n-1)
    
    x = stack1.pop()
    transfer(stack2, stack1, n-1)
    return x
	
# recursive popping using original stack and function call stack
def Pop(stack1):
    
    '''
    stack1: list
    '''
    if len(stack1) == 0:
        return -1
    if len(stack1) == 1:
        return stack1.pop()
    x = stack1.pop()
    item = Pop(stack1)
    stack1.append(x)
    return item
	
