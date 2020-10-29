'''
https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
Given preorder traversal of a binary search tree, construct the BST.
For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be the root of the following tree.

     10
   /   \
  5     40
 /  \      \
1    7      50
'''

# use min max concept, same as preorder to postorder
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def construct_tree(preorder, n):

    def buildTree(min_val, max_val):

        if prefix_ind[0] == n:
            return None

        if preorder[prefix_ind[0]] < min_val or preorder[prefix_ind[0]] > max_val:
             return None
        
        val = preorder[prefix_ind[0]]
        node = TreeNode(val)
        prefix_ind[0] += 1
        
        node.left = buildTree(min_val, val)
        node.right = buildTree(val, max_val)

        return node

    prefix_ind = [0]
    return buildTree(float('-inf'), float('inf'))

def printTree(root):
    if root == None:
        return 
    
    print(root.data, end = ' -> ')
    printTree(root.left)
    printTree(root.right)

preorder = [10, 5, 1, 7, 40, 50]
root = construct_tree(preorder, len(preorder))
printTree(root)