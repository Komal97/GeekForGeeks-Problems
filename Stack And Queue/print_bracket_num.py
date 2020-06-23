'''
https://practice.geeksforgeeks.org/problems/print-bracket-number/0
Given an expression exp of length n consisting of some brackets. The task is to print the bracket numbers when the expression is being parsed.
Input:
3​
(a+(b*c))+(d/e)​
((())(()))
((((()
Output:
1 2 2 1 3 3
1 2 3 3 2 4 5 5 4 1
1 2 3 4 5 5

Explanation:
Test case 1:The highlighted brackets in the given expression (a+(b*c))+(d/e) has been assigned the numbers as: 1 2 2 1 3 3.
'''
# keep a count, when '(' encountered, push and print count and when ')' encountered, print top and pop
def print_bracket(exp):
    count = 0
    stack = []
    for ch in exp:
        if ch == '(':
            count += 1
            print(count, end = " ")
            stack.append(count)
        elif ch == ')':
            print(stack[-1], end = " ")
            stack.pop()
    print()

if __name__ == '__main__':
    t = int(input())
    while t:
        exp = input()
        bracket_num(exp)
        t -= 1