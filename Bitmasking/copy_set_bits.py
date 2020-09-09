'''
https://practice.geeksforgeeks.org/problems/copy-set-bits-in-range/0
Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.
Each test case contains space separated values of x, l, r and y in a single line.
Input:
2
44 1 5 3
16 1 3 2

Output:
47
18
'''

# method - 1 - O(l-r)
# loop from l to r
# if ith bit is set in y (and) then set it in x (or)
def copy_set_bit(x, l, r, y):
    
    for i in range(l-1, r):
        mask = (1<<i)
        if (y&mask):
            x |= mask
    print(x)

# method - 2 O(1)
# y = 10101010101
# x = 10010011001
# l = 3, r = 7
def copy_set_bit(x, l, r, y):
    # create m1 = 0001111100
    mask1 = (1 <<(r-l+1))           # 00000100000
    mask1 -= 1                      # 00000011111
    mask1 = mask1<<(l-1)            # 00001111100
    
    # create m2 = 0001010100
    mask2 = (y&mask1)               # 00001111100 & 10101010101 = 0001010100
    x = x|mask2                     # x = 10010011001 | mask2 = 0001010100 => ans = 10011111101
    print(x)
    
t = int(input())
while t:
    x, l, r, y = list(map(int, input().split()))
    copy_set_bit(x, l, r, y)
    t -= 1