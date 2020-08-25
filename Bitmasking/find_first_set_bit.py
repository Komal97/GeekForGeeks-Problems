'''
https://practice.geeksforgeeks.org/problems/find-first-set-bit/0
Given an integer an N. The task is to print the position of first set bit found from right side in the binary representation of the number.
Input:
2
18
12

Output:
2
3

Explanation:
Testcase 1: Binary representation of the 18 is 010010, the first set bit from the right side is at position 2.
'''

# Take two's complement of the given no as all bits are reverted except the first '1' from right to left (0100)
# Do a bit-wise & with original no, this will return no with the required one only (0100)
# Take the log2 of the no, you will get position
# this is same as that of finding 1 set position or power of two
import math
def find_position(n):
    
    if n == 0:
        print(0)
        return
    two_complement = n&-n                           
    pos = int(math.log2(two_complement)) + 1
    
    print(pos)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        find_position(n)
        t -= 1