'''
https://practice.geeksforgeeks.org/problems/height-of-heap/0
Given a Binary Heap of size N, write a program to calculate the height of the Heap.
Input:
2
6
1 3 6 5 9 8
9
3 6 9 2 15 10 14 5 12
Output:
2
3
Explanation:
Testcase 1:

Input : N = 6
Output : 2
        (1)
       /    \
     (3)     (6)
    /  \    /
  (5)  (9) (8)
'''

# method - 1, since it is complete binary tree so total nodes in left most is total height
def height(arr, n):
    
    count = -1
    
    start = 0 
    
    while start < n:
        count += 1
        start = (2*start) + 1
    return count

# method - 2, using formula, count = log2(n)
import math
def height(arr, n):
    return int(math.log2(n))

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(height(arr, n))
        t -= 1
        