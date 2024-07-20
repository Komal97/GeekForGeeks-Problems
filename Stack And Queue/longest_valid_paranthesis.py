'''
https://practice.geeksforgeeks.org/problems/valid-substring/0
Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid substring.
NOTE: Length of smallest the valid substring ( ) is 2.
Input
4
(()(
()()((
((()()())))
()(())(

Output
2
4
10
6

Explanation:
Test Case 1: (()(
The longest valid substring is "()". Length = 2
'''
# method - 1, O(n^2) approach
# create all substrings and check whether it is balanced or not, if it is then store that substring length as count and keep track of maximum
def isBalanced(i, j, exp):
    
    stack = []
    exp = exp[i:j]
    for ch in exp:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack)==0
    
def valid_substring(exp):
    
    count = 0
    n = len(exp)
    for i in range(n):
        for j in range(i+1, n+1):
            if isBalanced(i, j, exp):
                count = max(count, j-i)
                
    print(count)        

# method - 2, O(n) time & O(n) space - using stack
# append -1 initially, if ( is encounter, append its index, if ) is encounter, then pop element and find length using current index and last balanced index 
# eg - ()(()))
def valid_substring(exp):
    n = len(exp)
    count = 0
    stack = [-1]
    
    for i in range(n):
        #If opening bracket, push index of it
        if exp[i] == '(':
            stack.append(i)
        # If closing bracket, i.e.,str[i] = ')'
        else:
            # If the stack is not empty and on the top is the index of a open bracket then pop
            stack.pop()
            if len(stack) > 0:
                count = max(count, i-stack[-1])
            # If stack is empty. push current index as base for next valid substring (if any)
            else:
                stack.append(i)
    return count
            
	
	
# method - 3, O(n) time & O(1) space
# counter left for '(' and counter right for ')'
# traverse from left to right & increment counter, if left = right then save that length is max, right > left then set left = right = 0
# same traverse from right to left, if left > right then left = right = 0
def valid_substring(exp):
    
    l = 0
    r = 0 
    count = 0
    n = len(exp)
    for i in range(n):
        if exp[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            count = max(count, 2*r)
        if r>l:
            l = r = 0
    l = r = 0
    for i in range(n-1, -1, -1):
        if exp[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            count = max(count, 2*r)
        if l>r:
            l = r = 0
    return count

if __name__ == '__main__':
    t = int(input())
    while t:
        exp = input()
        valid_substring(exp)
        t -= 1