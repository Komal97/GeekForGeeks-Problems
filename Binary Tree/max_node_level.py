'''
https://practice.geeksforgeeks.org/problems/maximum-node-level/1
Given a Binary tree. Find the level in binary tree which has the maximum number of nodes.
Input:
2
2 1 3 4 6 N 8 N N 5
1 2 
Output:
2
0

Explanation:
Test Case 1: The given Binary Tree is:
      2
    /    \ 
  1      3
 /   \      \
4    6     8
     / 
    5
'''

# in queue, at each point we have total number of nodes of each level
# by finding length of queue, we get number of nodes at each level
from collections import deque
def maxNodeLevel(root):
    q = deque()
    q.append(root)
    
    maxsize = float('-inf')
    maxlevel = 0
    level = 0
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if maxsize<size:
            maxsize = size
            maxlevel = level
        level += 1
    return maxlevel
