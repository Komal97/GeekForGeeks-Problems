'''
https://www.geeksforgeeks.org/merge-two-binary-trees-node-sum/
Given two binary trees. We need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of new tree.
Example:
Input: 
     Tree 1            Tree 2                  
       2                 3                             
      / \               / \                            
     1   4             6   1                        
    /                   \   \                      
   5                     2   7                  

Output: Merged tree:
         5
        / \
       7   5
      / \   \ 
     5   2   7
'''

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        if not A:
            return B
        elif not B:
            return A
        
        A.val += B.val
        A.left = self.solve(A.left, B.left)
        A.right = self.solve(A.right, B.right)
        return A
        
            