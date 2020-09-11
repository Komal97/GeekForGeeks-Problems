'''
https://practice.geeksforgeeks.org/problems/bleak-numbers/0
Given an integer, check whether it is Bleak or not. 
A number ‘n’ is called Bleak if it cannot be represented as sum of a positive number x and set bit count in x, i.e., x + countSetBits(x) is not equal to n for any non-negative number x.
Input:
3
4
167
3

Output:
1
0
0
Explanation:
4 is t Bleak as it cannot be represented as sum of a number x and countSetBits(x) for any number x.
3 is not Bleak as it can be represented as 2 + countSetBits(2).
'''


from math import log2
def countsetbits(n):
    count = 0
    while n:
        n = (n&n-1)
        count += 1
    return count
    
def checkBleak(n):
    
    maxlimit = int(log2(n))+1
    for i in range(n-maxlimit, n, 1):
        if (i + countsetbits(i)) == n:
            return 0
    return 1
    
    
t = int(input())
while t:
    n = int(input())
    ans = checkBleak(n)
    print(ans)
    t -= 1