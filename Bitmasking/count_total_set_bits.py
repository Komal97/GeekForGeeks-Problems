'''
https://practice.geeksforgeeks.org/problems/count-total-set-bits/0
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
Input:
2
4
17
Output:
5
35

Explanation:
Testcase1:
An easy way to look at it is to consider the number, n = 4:
0 0 0 = 0
0 0 1 = 1
0 1 0 = 1
0 1 1 = 2
1 0 0 = 1
Therefore , the total number of bits is 5.
'''

# method - 1 => time - O(k*n) where is number of set bits, space - O(1)
def count_set_bits(n):
    
    count = 0
    for i in range(1, n+1):
        num = i
        while num:
            num = num&(num-1)
            count += 1
            
    print(count)

# method - 2 => time - O(n), space - O(n) 
# if number is even, then it has number of bits same as i/2 (dp[i]=dp[i//2) because when number is multiply by 2, then bits are shifted only
# if number is odd, then it has number of bits same as (i/2)+1 (dp[i]=dp[i//2]+1) because in this case, bits are shifted and 1 bits is added at 0th position
def count_set_bits(n):
    
    count = 1
    dp = [0]*(n+1)
    dp[1] = 1
    
    for i in range(2, n+1):
        if i%2 == 0:
            dp[i] = dp[i//2]                
        else:
            dp[i] = dp[i//2] + 1
        
        count += dp[i]

    print(count)

# method - 3 => time - O(log n)
from math import log2
def count_set_bits(n):
    
    if n == 0 or n == 1:
        return n
    
    x = int(log2(n))                                            # find max power 2
    bitsupto2raisex = x*(1<<(x-1))          # 2^(x-1) * x       # find (2^x / 2)*x    
    msbupto2raisexton = n - (1<<x) + 1      # n - 2^x + 1       # remaining = n -(2^x)+1
    rest = n - (1<<x)
    ans = bitsupto2raisex + msbupto2raisexton + count_set_bits(rest)
    return ans
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        count_set_bits(n)
        t -= 1