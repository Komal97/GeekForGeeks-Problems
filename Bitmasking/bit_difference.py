'''
https://practice.geeksforgeeks.org/problems/bit-difference/0
You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.
Input:
1
10 20
Output:
4

Explanation:
Testcase1:
A  = 01010
B  = 10100
Number of bits need to flipped = 4
'''

# find xor of 2 numbers, give a number with set bits which are difference in both num
# then find number of set bits using rightmost set bit logic
t = int(input())
while t:
    a, b = list(map(int, input().split()))
    
    flipped = a^b
    count = 0
    while flipped:
        rsbm = (flipped & -flipped)
        flipped -= rsbm
        count += 1
    print(count)
    
    t -= 1
    