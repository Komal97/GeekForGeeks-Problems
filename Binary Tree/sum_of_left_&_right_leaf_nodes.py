'''
https://practice.geeksforgeeks.org/problems/sum-of-left-leaf-nodes/1
Given a Binary Tree of size N. Find the sum of all the leaf nodes that are left child of their parent of the given binary tree.
Example:

Input : 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
  /  \        /  \
 7    2      6    9
Output :
sum = 6 + 7 = 13
Input:
2
1 2 3
10 20 30 40 60 90
Output:
2
130
'''

# keep parent and child node
# check for 2 leaf nodes of parent
# add left leaf parent data to sum 
def leftLeavesSum(root_node):
    
    def leftSum(node, parent, summ):
        if node == None:
            return 0
        
        if parent != None and node.left == None and node.right == None:
            if parent.left == node:
                summ += node.data
                return summ
        lsum = leftSum(node.left, node, summ)
        rsum = leftSum(node.right, node, summ)
        return lsum + rsum
    return leftSum(root_node, None, 0)


'''
https://practice.geeksforgeeks.org/problems/sum-of-right-leaf-nodes/1
Given a Binary Tree of size N, your task is to complete the function rightLeafSum(), that should return the sum of all the leaf nodes that are right child of their parent of the given binary tree.
Example:

Input : 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
     \        /  \
      2       6   7
Output :
sum = 2 + 5 + 7 = 14
Input:
2
2
1 2 L 1 3 R
5
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L
Output:
3
60
'''

# keep parent and child node
# check for 2 leaf nodes of parent
# add right leaf parent data to sum 
def rightLeafSum(root):
    
    def rightSum(node, parent, summ):
        if node == None:
            return 0
        
        if parent != None and node.left == None and node.right == None:
            if node == parent.right:
                summ += parent.right.data
                return summ
            
        lsum = rightSum(node.left, node, summ)
        rsum = rightSum(node.right, node, summ)
        return lsum + rsum
    return rightSum(root, None, 0)