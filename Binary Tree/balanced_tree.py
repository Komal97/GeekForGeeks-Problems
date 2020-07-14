'''
https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

Input:
3
1 2 N N 3
10 20 30 40 60 N N
4 6 6
Output:
0
1
1
Explanation:
Testcase1: The tree is
        1
     /    
   2
      \
       3 
The max difference in height of left subtree and right subtree is 2, which is greater than 1. Hence unbalanced.
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
The max difference in height of left subtree and right subtree is 1. Hence balanced.
'''

# create a custom pair class with current height and subtree balanced or not
# check left tree is balance tree, right tree is balance tree and diff b/w left height and right height which should be -1, 0, 1 or abs(diff)<=1
class Pair:
    def __init__(self):
        self.height = 0
        self.isBalance = True
        
def checkBalanced(root):
    if root == None:
        p = Pair()
        return p
    
    leftbal = checkBalanced(root.left)
    rightbal = checkBalanced(root.right)
    
    cur_pair = Pair()
    cur_pair.height = max(leftbal.height, rightbal.height) + 1
    diff = abs(leftbal.height - rightbal.height)
    cur_pair.isBalance = leftbal.isBalance and rightbal.isBalance and (diff<=1)
    
    return cur_pair

def isBalanced(root):
    if root == None:
        return True
    pair = checkBalanced(root)
    return pair.isBalance