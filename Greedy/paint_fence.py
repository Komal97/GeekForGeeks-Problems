'''
https://practice.geeksforgeeks.org/problems/painting-the-fence/0
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. 
Since answer can be large return it modulo 10^9 + 7.
Input:
2
2 4
3 2

Output:
16
6
'''

M = 1000000007
def paint_fence(n, k):
    
    same = k*1                              # only way to add same colour in prv is 1      
    diff = k*(k-1)                          # only way to add diff colour in prv is k-1 i.e. exclude same colour
    total = same + diff
    
    for i in range(3, n+1):
        same = diff                         # same can only be added to diff to make 2 consecutive
        diff = (total*(k-1))%M              # add diff k-1 colours to prv (if prv = red then add green & blue)
        total = (same+diff)%M
    
    print(total)

t = int(input())
while t:
    n, k = list(map(int, input().split()))
    paint_fence(n, k)
    t -= 1
    
