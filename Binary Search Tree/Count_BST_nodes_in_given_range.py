'''
https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1
Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.

The values smaller than root go to the left side
The values greater and equal to the root go to the right side
Input:
2
6
10 5 50 1 40 100
5 45
5
5 6 7 4 3
2 8

Output:
3
5
'''

# check each node whether it lies in given range or not
def count(root, l, h, c):
    if root == None:
        return
    
    count(root.left, l, h, c)
    if root.data >= l and root.data <= h:
        c[0] += 1
    
    count(root.right, l, h, c)
    
def getCountOfNode(root,l,h):
    
    c = [0]
    count(root, l, h, c)
    return c[0]

# another method for code
def getCountOfNode(root,l,h):
    
    # base condition
    if root == None:
        return 0
    
   
    # if root lie in range then current node + no of nodes from left + no of node fron right tree
    if root.data >= l and root.data <= h:
        return 1 + getCountOfNode(root.left,l,h) + getCountOfNode(root.right,l,h)

    # else if root node is less than l then check in right tree
    elif root.data < l:
        return getCountOfNode(root.right,l,h)
    # else check left tree
    return getCountOfNode(root.left,l,h)