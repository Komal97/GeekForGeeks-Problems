'''
https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/
Given an integer n, calculate the square of a number without using *, / and pow(). 

Examples : 
Input: n = 5
Output: 25

Input: 7
Output: 49

Input: n = 12
Output: 144
'''

# if n = even then n = (2x)^2 = 4x^2
# if n = odd then n = (2x + 1)^2 = 4x^2 + 4x + 1
# x = n/2 from first assumption
def square(n):
    if n == 0:
        return 0
    
    if n < 0:
        return -n

    x = n>>1
    
    if n&1:
        return ((square(x)<<2) + (x<<2) + 1)
    else:
        return (square(x)<<2)
    
for i in range(1, 10):
    print(square(i))