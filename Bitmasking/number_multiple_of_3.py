'''
https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0
Given a binary number, write a program that prints 1 if given binary number is a multiple of 3.  Else prints 0. The given number can be big upto 2^100. It is recommended to finish the task using one traversal of input binary string.
Input:
2
011
100

Output:
1
0
'''

# (number of odd set bits - number of even set bits)%3
t = int(input())
while t:
    inp = input()
    n = len(inp)
    even_bits = 0
    odd_bits = 0
    for i in range(n-1, -1, -1):
        if inp[n-i-1] == '1':
            if ((n-i-1)&1) :
                odd_bits += 1
            else:
                even_bits += 1
 
    if (abs(odd_bits-even_bits))%3 == 0:
        print(1)
    else:
        print(0)
    t -= 1