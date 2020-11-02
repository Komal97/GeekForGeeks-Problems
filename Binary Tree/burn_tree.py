'''
https://www.geeksforgeeks.org/burn-the-binary-tree-starting-from-the-target-node/
Given a binary tree denoted by root node A and a leaf node B from this tree.
It is known that all nodes connected to a given node (left child, right child and parent) get burned in 1 second. Then all the nodes which are connected through one intermediate get burned in 2 seconds, and so on.
Input : 
                       12
                     /     \
                   13       10
                          /     \
                       14       15
                      /   \     /  \
                     21   24   22   23
target node = 14
Output :
14
21, 24, 10
15, 12
22, 23, 13

Explanation : First node 14 burns then it gives fire to it's 
neighbors(21, 24, 10) and so on. This process continues until 
the whole tree burns.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
from collections import deque
sys.setrecursionlimit(10000)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        q = deque()
        time = 0
        
        def burnUtil(root):
            nonlocal time
            
            if not root:
                return 0
                
            if root.val == B:
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                    
                print(root)
                return 1
            
            a = burnUtil(root.left)
            if a == 1:
                
                # add time
                time += 1
                size = len(q)
                for i in range(size):
                    
                    node = q.popleft()
                    print(node, end = ' ')
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                print(root)
                if root.right:
                    q.append(root.right)
                return 1
                
            b = burnUtil(root.right)
            if b == 1:
                # add time
                time += 1
                size = len(q)
                for i in range(size):
                    
                    node = q.popleft()
                    print(node, end = ' ')
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                print(root)
                if root.left:
                    q.append(root.left)
                return 1
            
            return 0
        
        burnUtil(A)
        
        while len(q):
            size = len(q)
            for i in range(size):
                
                node = q.popleft()
                print(node, end = ' ')
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            print()
            # add time
            time += 1
        
        return time