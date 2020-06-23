'''
https://practice.geeksforgeeks.org/problems/infix-to-postfix/0
Given an infix expression in the form of a string str. Conver this infix expression to postfix expression.
Input:
2
a+b*(c^d-e)^(f+g*h)-i
A*(B+C)/D

Output:
abcd^e-fgh*+^*+i-
ABC+*D/
'''
# As soon as operand is encounter, append in output and keep a stack and push operators and append operators in output according to precedence
def isOperand(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '^' or ch == '(' or ch == ')':
        return False
    return True

def precedence(ch):
    if ch == '^':
        return 3
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    return 0

def infix_to_postfix(infix):
    postfix = ''
    i = 0
    n = len(infix)
    stack = []
    while i<n:
        ch = infix[i]
        if isOperand(ch):
            postfix += ch
            i += 1
        else:
            if ch == '(':
                stack.append(ch)
                i += 1
            elif len(stack) == 0 or precedence(ch) > precedence(stack[-1]):
                stack.append(ch)
                i += 1
            elif len(stack) > 0 and ch == ')' and stack[-1] != '(':
                postfix += stack.pop()
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
                i += 1
            else:
                postfix += stack.pop()
    while len(stack) > 0:
        postfix += stack.pop()
    print(postfix)

if __name__ == '__main__':
    t = int(input())
    while t:
        infix = input()
        infix_to_postfix(infix)
        t -= 1