'''
https://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1
Given a binary tree, your task is to complete the function minDepth which takes one argument the root of the binary tree and prints the min depth of  binary tree
Input:
2
1 3 2 4
10 20 30 N 40 N 60 N N 2
Output:
2
3

Explanation:
         1
       /   \
     2      3
    /        
   4       

For the tree above the min depth is 2 ie 1 3
'''

# RECURSIVE
def minDepth(root):
    # if root == None:
    #     return 0
    # lh = minDepth(root.left) 
    # rh = minDepth(root.right)
    
    # if root.left != None and root.right == None:
    #     return lh+1
        
    # if root.right != None and root.left == None:
    #     return rh+1
        
    # return min(lh, rh) + 1
    
    # base condition if tree is None
    if root == None:
        return 0
    
    # leaf node has height 1
    if root.left == None and root.right == None:
        return 1
        
    # if left subtree is None then height from right subtree is counted
    # if right subtree is None then height from left subtree is counted
    lh = minDepth(root.left) if root.left != None else float('inf')
    rh = minDepth(root.right) if root.right != None else float('inf')
        
    return min(lh, rh) + 1

# ITERATIVE
# first leaf node encountered is min depth
from collections import deque
def minDepth(root):
    
    # if tree is None
    if root == None:
        return 0
    
    # if root node is leaf node
    if root.left == None and root.right == None:
        return 1
        
    q = deque()
    
    # push (node, level) in queue
    q.append((root, 1))
    
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node, level = q.popleft()
            # first encountered leaf node level is minlevel
            if node.left == None and node.right == None:
                return level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
    return 0
   