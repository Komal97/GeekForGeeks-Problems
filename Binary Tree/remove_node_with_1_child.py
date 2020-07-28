'''
https://practice.geeksforgeeks.org/problems/remove-half-nodes/1
Given A binary Tree. Your task is to remove all the half nodes (which has only one child).
Input:
2
7 7 8 2
2 7 5 N 6 N 9 1 11 4
Output:
2 7 8 
1 6 11 2 4

Explanation:
Test Case 1: The given tree is:
      7
    /    \
  7      8
 /
2
Modified tree after removing this node is:
      7
    /    \ 
   2     8
The in-order traversal of this tree is: 2 7 8
'''

# same as deletion in BST with one child in postorder
def RemoveHalfNodes(root): 
    
    if root == None:
        return None
        
    root.left = RemoveHalfNodes(root.left)
    root.right = RemoveHalfNodes(root.right)
    
    if root.left != None and root.right == None:
        temp = root.left
        del root
        return temp
    
    if root.left == None and root.right != None:
        temp = root.right
        del root
        return temp
        
    return root