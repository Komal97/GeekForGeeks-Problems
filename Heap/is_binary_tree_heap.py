'''
https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1
Given a binary tree you need to check if it follows max heap property or not.
Input:
2
2
5 2 L 5 3 R
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
1
0
'''

from collections import deque

# using level order, check 2 properties
# check complete binary tree using flag
# check left data with root and right data with root 
def isHeap(root):
    
    if root == None:
        return True
    
    q = deque()
    q.append(root)
    
    flag = False
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                if flag == True:                # if we see node before which no right node of prv parent
                    return False
                if node.left.data > node.data:  # check parent data with child data
                    return False
                q.append(node.left)
            else:
                flag = True                     # change flag to denote that left child is missing
            if node.right:
                if flag == True:                # if we see node before which no left node occur of same parent
                    return False
                if node.right.data > node.data: # check parent data with child data
                    return False
                q.append(node.right)
            else:
                flag = True                     # change flag to denote that right child is missing

    return True
    
