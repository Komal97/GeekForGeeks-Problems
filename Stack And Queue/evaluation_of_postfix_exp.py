'''
https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression/0
Given a postfix expression, the task is to evaluate the expression and print the final value. 
Operators will only include the basic arithmetic operators like *,/,+ and - .
Input:
2
231*+9-
123+*8-
Output:
-4
-3
'''
# if number encounter, push in stack, else pop 2 elements from top, evaluate them and push again in stack
# return last left lement
def evaluation(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a//b
        
def postfix_eval(expression):
    
    stack = []
    for ch in expression:
        if ch != '+' and ch != '-' and ch != '*' and ch != '/':
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(evaluation(a, b, ch))
    print(stack[-1])
    
if __name__ == '__main__':
    t = int(input())
    while t:
        expression = input()
        postfix_eval(expression)
        t-=1