'''
https://practice.geeksforgeeks.org/problems/reverse-bits/
Given a 32 bit number x, reverse its binary form and print the answer in decimal.
Input:
2
1
5
Output:
2147483648
2684354560

Explanation:
Testcase1:
00000000000000000000000000000001 =1
10000000000000000000000000000000 =2147483648s
'''

# method - 1 => if 1<<i is set in num then set 1<<(maxbits-i-1) in reversenum
# time - O(n), space - O(1)
def reverse_bits(n):
    
    maxbits = 32
    
    reversenum = 0
    for i in range(32):
        temp = n&(1<<i)
        if temp:
            reversenum = reversenum|(1<<(maxbits-i-1))
    
    print(reversenum)
    
# method - 2 => number is shifted right, and reversed is shifted left until n != 0, after that set rest bits as 0 from right
# time - O(log n), space - O(1)
def reverse_bits(n):
    
    count = 32
    rev = 0
    while n:
        rev = rev << 1                  # reverse is shifted left
        rev |= n&1                      # add righmost bit to reversed
        n >>= 1                         # num is shifted right 
        count -= 1
        
    while count:                        # set rest bits as 0 from right
        rev = rev << 1
        count -= 1
    
    print(rev)
        
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        reverse_bits(n)
        t -= 1
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        reverse_bits(n)
        t -= 1