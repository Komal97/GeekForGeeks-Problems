'''
https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1
Your task is to implement  2 stacks in one array efficiently 
Expected Time Complexity: O(1) for all the four methods.
Expected Auxiliary Space: O(1) for all the four methods.
Input
2
6
1 1 2 1 1 3 2 1 4 1 2 2 2 2 2
4
1 1 2 2 2 1 2 2 2
Output
3 4 -1
-1 2 -1

Explanation:
Testcase1:
1 1 2    the stack1 will be {2}
1 1 3    the stack1 will be {2,3}
2 1 4   the stack2 will be {4}
1 2      the poped element will be 3 from stack1 and stack1 will be {2}
2 2      the poped element will be 4 from stack2 and now stack2 is empty
2 2      the stack2 is now empty hence -1 .
'''
# for stack1 - insert from starting and for stack2 - insert from end
# space efficicient - as if elements not in stack2 and space in array is available then elements of stack1 can be stored which is not possible if we divide array into 2 halves

def pop1(a):
    global top1
    x = -1
    if top1 <= top2 and top1>-1:
        x = a[top1]
        top1 -= 1
    return x
        
def pop2(a):
    global top2
    x = -1
    if top1 <= top2 and top2<101:
        x = a[top2]
        top2 += 1
    return x
    
def push1(a,x):
    global top1
    if top1 <= top2:
        top1 += 1
        a[top1] = x
    
def push2(a,x):
    global top2
    if top1 <= top2:
        top2 -= 1
        a[top2] = x