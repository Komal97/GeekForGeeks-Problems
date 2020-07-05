'''
https://practice.geeksforgeeks.org/problems/permutation-with-spaces/0
Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them. Output should be printed in sorted increasing order of strings.

Input:
2
AB
ABC

Output:
(A B)(AB)
(A B C)(A BC)(AB C)(ABC)
'''

# at every step we have 2 choices, either add character in output or space + character in output
def permutation_with_spaces(s, output):
    if len(s) == 0:
        print('(', end = '')
        print(output, end = '')
        print(')', end = '')
        return
    permutation_with_spaces(s[1:], output + ' ' + s[0])
    permutation_with_spaces(s[1:], output + s[0])


if __name__ == '__main__':
    t = int(input())
    while t:
        s = input()
        output = s[0]
        permutation_with_spaces(s[1:], output)
        print()
        t -= 1