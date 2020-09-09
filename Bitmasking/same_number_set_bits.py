'''
https://www.geeksforgeeks.org/number-set-bits-n/
Given a positive integer N, find out how many positive integers strictly less than N have the same number of set bits as N.
Input: 8
Output: 3
Input: 1
Output: 0

Explanation:
Test Case 1:
Binary representation of 8 : 1000, so number of set bits in 8 is 1.
So the integers less than 8 with same number of set bits are : 4, 2, 1
'''

def ncr(n, r):
    if n < r:
        return 0
    
    # expand nCr and cancel out (n-r)! in numerator and denominator
    # then find it
    res = 1
    for i in range(r):                          
        res *= (n-i)            # numerator = n*(n-1)*(n-2)*(n-r-1)
        res //= (i+1)           # denominator = 1*2*3*.....r
    return res
    
def count_set_bits(n):
    
    count = 0
    while n:
        rsbm = (n&-n)
        n -= rsbm
        count+= 1
    return count
    
def solution(n, k, i):
    if i == 0:
        return 0
        
    mask = 1 << i                           # mask of most significant bit
    res = 0
    if (n & mask) == 0:                     # check MSB is 0
        res = solution(n, k, i-1)           # then call on i-1 bits with same set bits on
    else:                                   # if MSB is 1
        res1 = solution(n, k-1, i-1)        # then call on i-1 bits with k-1 bits by considering current bit as 1
        res0 = ncr(i, k)                    # find nCr ways where n=i and r=k by considering current bit as 0 
        res = res1 + res0                   
        
    return res
    
n = int(input())
set_bits = count_set_bits(n)
ans = solution(n, set_bits, 63)
print(ans)