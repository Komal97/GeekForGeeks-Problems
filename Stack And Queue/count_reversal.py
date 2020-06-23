'''
https://practice.geeksforgeeks.org/problems/count-the-reversals/0
Given a string S consisting only of opening and closing curly brackets '{' and '}' 
find out the minimum number of reversals required to make a balanced expression.
Input
4
}{{}}{{{
{{}}}}
{{}{{{}{{}}{{
{{{{}}}}

Output
3
1
-1
0

Explanation:
Testcase 1: For the given string }{{}}{{{ since the length is even we just need to count the number of openning brackets('{') 
suppose denoted by 'm' and closing brackest('}') suppose dentoed by 'n' after removing highlighted ones. After counting compute ceil(m/2) + ceil(n/2).
'''
# eliminate balanced expressions and maintain m, n for '{' & '}' as count for unbalanced expression
# in unbalanced, half of { are unbalanced and same with }, so add their count and find their half
# but we add 1 if they are odd as m = 11, n = 1 then 10 out of 11 are balanced and we need 1 to maintain n
def count_reversal(exp):
    length = len(exp)
    if length%2 != 0:
        return -1
    m = 0
    n = 0
    stack = []
    for i, ch in enumerate(exp):
        if ch == '{':
            stack.append(ch)
            m += 1
        elif ch == '}':
            n += 1
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
                n -= 1
                m -= 1
                
    return ((m+n)//2) + (n%2)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        exp = input()
        print(count_reversal(exp))
        t -= 1