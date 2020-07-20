'''
https://practice.geeksforgeeks.org/problems/largest-bst/1
Given a binary tree. Find the size of its largest subtree that is a Binary Search Tree.
Input
2
1 4 4 6 8
6 6 3 N 2 9 3 N 8 8 2

Output
1
2

Explanation:
Test Case 1: There's no sub-tree with size greater than 1 which forms a BST. All the leaf Nodes are the BSTs with size equal to 1.
Test Case 2: The following sub-tree is a BST of size 2: 
      2
    /   \ 
  N      8
'''

class Pair:
    def __init__(self):
        self.isBal = True
        self.min_val = float('inf')
        self.max_val = float('-inf')
        self.largestroot = None
        self.size = 0
 
# use the concept of isbalanced BST with custom class and maintain largest balanced subtree root and size in class
def largestBst(root):
    
    def checkLargest(root):
        if root == None:
            basepair = Pair()
            return basepair
        
        lpair = checkLargest(root.left)
        rpair = checkLargest(root.right)
        
        mypair = Pair()
        mypair.isBal = lpair.isBal and rpair.isBal and root.data>lpair.max_val and root.data<rpair.min_val
        mypair.min_val = min(root.data, min(lpair.min_val, rpair.min_val))
        mypair.max_val = max(root.data, max(lpair.max_val, rpair.max_val))
        
        # if tree with current node is balanced then it is largest BST
        if mypair.isBal:
            mypair.largestroot = root
            mypair.size = lpair.size + rpair.size + 1
        # else if left subtree has largest BST then return that else largest BST must be in right subtree
        else:
            if lpair.size > rpair.size:
                mypair.largestroot = lpair.largestroot
                mypair.size = lpair.size 
            else:
                mypair.largestroot = rpair.largestroot
                mypair.size = rpair.size 
                
        return mypair
    return checkLargest(root).size