'''
https://practice.geeksforgeeks.org/problems/delete-nodes-greater-than-k/1
Given a BST and a value x, the task is to delete the nodes having values greater than or equal to x.
Input:
2
7
20 8 22 4 12 10 14
8
7
20 8 22 4 12 10 14
10
Output:
4
4 8
'''

# use postorder traversal, because if leaf nodes are deleted then root node can be delete easily
# delete node on left and attach new root to left, delete node on right and attach new root to right recursively
# if root node >= X, delete root node(root node can have 0 or 1 child)
# if 0 child then temp become None else temp will have left child, right has greater values and due to postorder, those must be deleted 

def deleteNode(root, X):
    
    if root == None:
        return None
    
    # delete node from left and attach new root
    root.left = deleteNode(root.left, X)
    # delete node from right and attach new root
    root.right = deleteNode(root.right, X)
    # delete root node(root node can have 0 or 1 child) 
    if root.data >= X:
        temp = root.left
        del root
        return temp
    return root 