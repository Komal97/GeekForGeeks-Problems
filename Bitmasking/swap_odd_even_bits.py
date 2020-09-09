'''
https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits/0
Given an unsigned integer N. The task is to swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43(00101011). 
Here, every even position bit is swapped with adjacent bit on right side(even position bits are highlighted in binary representation of 23), and every odd position bit is swapped with adjacent on left side.
Input:
2
23
2
Output:
43
1
Explanation:
Testcase 1: BInary representation of the given number; 00010111 after swapping 00101011.
'''

def swap_bits(n):
     
    even = (n & 0xAAAAAAAA)             # find even bits
    odd = (n & 0x55555555)              # find odd bits
    even >>= 1                          # right shift even bits, means even place bits are at odd place
    odd <<= 1                           # left shift odd bits, means odd place bits are at even place
    
    n = odd | even                      # n = odd|even
    print(n)                                                    

t = int(input())
while t:
    n = int(input())
    swap_bits(n)
    t -= 1
