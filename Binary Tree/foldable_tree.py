'''
https://practice.geeksforgeeks.org/problems/foldable-binary-tree/1
Given a binary tree, check if the tree can be folded or not. A tree can be folded if left and right subtrees of the tree are structure wise same. An empty tree is considered as foldable.
Input:
2
10 7 15 N 9 11 N
10 7 15 5 N 11 N
Output:
Yes
No

Explanation:
Testcase 1: Given tree is
                              10
                           /      \
                         7         15
                      /      \  /      \
                    N      9    11     N
Hence, above tree is structure wise same so it is foldable.
Testcase 2: Given tree is 
                                10
                            /       \
                          7           15
                       /    \       /    \
                     5        N    11      N
Hence, above tree is not structure wise same so it is not foldable.
'''

# same as symmetric tree, check only structure not value, left and right tree should be symmetric
def IsFoldable(root):
    
    if root == None:
        return True
        
    def checkFoldable(root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        lbool = checkFoldable(root1.left, root2.right)
        rbool = checkFoldable(root1.right, root2.left)
        return lbool and rbool 
        
    return checkFoldable(root.left, root.right)