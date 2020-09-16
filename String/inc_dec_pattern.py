'''
https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0
Given a pattern containing only I's and D's. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern.
Digits from 1-9 and digits can't repeat.
Input
5
D
I
DD
IIDDD
DDIDDIID

Output
21
12
321
126543
321654798
'''

def create_number(exp, n):
    
    result = ''
    stack = []
    for i in range(n+1):
        stack.append(i+1)
        if i == n or exp[i] == 'I':
            while len(stack) > 0:
                result += str(stack[-1])
                stack.pop()
    return result

def create_number(exp, n):
    
    ans = [''] *(n+1)
    count = 1
    for i in range(n+1):
        # if current 'I' in encountered then, fill count in array from i until prev I or 0th index is not encountered
        if i == n or exp[i] == 'I':                             
            for j in range(i, -1, -1):
                if j!= n and exp[j] == 'I' and i!=j:
                    break
                ans[j] = str(count)
                count += 1
                
    return ''.join(ans)      

t = int(input())
while t:
    exp = input()
    ans = create_number(exp, len(exp))
    print(ans)
    t -= 1
