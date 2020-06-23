'''
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
'''

# if any opening bracket, push in stack
# if closing bracket, then check whether corresponding opening bracket is on top - if yes then pop out top, if not or stack is empty then not balanced 
def paranthesis_check(exp):
    stack = []
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
        elif ch == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
        elif ch == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return False
        if ch == ')' or ch == '}' or ch == ']':
            stack.pop()
   
    return len(stack) == 0
    
if __name__ == '__main__':
    t = int(input())
    while t:
        exp = input()
        if(paranthesis_check(exp)):
            print('balanced')
        else:
            print('not balanced')
        t -= 1