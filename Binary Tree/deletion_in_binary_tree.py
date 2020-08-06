'''
https://practice.geeksforgeeks.org/problems/deletion-in-a-binary-tree/1
Given a Binary Tree of size N, your task is to complete the function deletionBT(), that should delete a given node from the tree by making sure that tree shrinks from the bottom (the deleted node is replaced by bottommost and rightmost node).
Input:
2
1
1 4 7 5 6 
5
7 10 4 11 2 5 9 
Output:
5 4 6 7 
11 10 2 7 9 4 
'''

from collections import deque
def deletionBT(root, key):
    
    if root == None:
        return root
    
    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return root
    keynode = None      # node to be deleted
    lastnode = None     # last deepest node
    pl = None           # parent of left child
    pr = None           # parent of right child
    
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            lastnode = q.popleft()
            if lastnode.data == key:            # if search key found, then set keynode
                keynode = lastnode
            if lastnode.left:
                q.append(lastnode.left)
                pl = lastnode                   # set current node as parent of left child
                pr = None
            if lastnode.right:
                q.append(lastnode.right)
                pr = lastnode                   # set current node as parent of right child
                pl = None
    
    # if key to be deleted found then replace data with deepest last node 
    if keynode:                             
        keynode.data = lastnode.data             
        
        # set parent of deepest node to be null
        if pl:
            pl.left = None
        if pr:
            pr.right = None
            
    return root