'''
https://practice.geeksforgeeks.org/problems/print-bst-elements-in-given-range/1
Given a Binary Search Tree and a range. Print all the numbers in the BST that lie in the given range.
Input:
2
17 4 18 2 9 
4 24
16 7 20 1 10 
13 23
Output:
4 9 17 18 
16 20 

Explanation:
Testcase 1: For the given input, elements which lies in the range of 4 and 24(inclusive) are 4 9 17 18. The generated BST is:
       17
      /    \
    4     18
  /   \
2     9
'''

# if low < root data then move to left
# if root data is in range then print 
# if high > root data then move to right
# use inorder traversal to keep keys sorted
def addNodes(root, low, high, out):
    if root == None:
        return
    
    if low < root.data:
        addNodes(root.left, low, high, out)
        
    if root.data >= low and root.data <= high:
        out.append(root.data)
        
    if high >= root.data:
        addNodes(root.right, low, high, out)
    
def printNearNodes(root, low, high):
    
    out = []
    addNodes(root, low, high, out)
    return out
