'''
https://practice.geeksforgeeks.org/problems/diagonal-sum-in-binary-tree/1
Given a Binary Tree of size N, print all diagonal sums.
Input:
2
4 1 3 N N 3
10 8 2 3 5 2
Output:
7 4 
12 15 3 
'''

# same as vertical order
# while moving left d = d+1
# while moving right d = d
from collections import deque
def diagonalSum(root):
    
    q = deque()
    q.append((root, 0))
    h = {}
    
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node, d = q.popleft()
            if d in h:
                h[d] += node.data
            else:
                h[d] = node.data
            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d))
                
    h = sorted(h.items(), key = lambda x: x[0])
    ans = []
    for d, summ in h:
        ans.append(summ)
    return ans