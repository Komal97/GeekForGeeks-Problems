'''
https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
Given a string S. The task is to print all permutations of a given string.
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
'''

# method - 1 => for recursion, options are - choose character one by one as first chracter, remove and append in output 
def permutation(input_str, output):
    if input_str == '':
        print(output, end = ' ')
        return 
    
    for i in range(len(input_str)):
        ch = input_str[i]                       # choose a character
        left = input_str[0:i]                   # separate string left of chosen character
        right = input_str[i+1:]                 # separate string right of chosen character
        permutation(left+right, output+ch)      # removed choosen character is appended in output
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        input_str = input()
        input_str = ''.join(sorted(input_str))
        permutation(input_str, '')
        print()
        t -= 1
        
# method - 2 => we swap ith character with all characters after ith
# while returning, we swap back because for right call, we need original array
def permutation(input_str, i, n):
    if i == n:
        print(''.join(input_str), end = ' ')
        return
    
    for j in range(i, len(input_str)):
        input_str[i], input_str[j] = input_str[j], input_str[i]
        permutation(input_str, i+1, n)
        input_str[i], input_str[j] = input_str[j], input_str[i]
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        input_str = input()
        input_str = ''.join(sorted(input_str))
        permutation(list(input_str), 0, len(input_str))
        print()
        t -= 1