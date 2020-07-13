'''
https://practice.geeksforgeeks.org/problems/sum-of-leaf-nodes/1
Given a Binary Tree of size N. The task is to complete the function sumLeaf(), that should return the sum of all the leaf nodes of the given binary tree.
Input:
For each testcase, there will be two lines, first of which containing the number of edges (between two nodes) in the tree. 
Next line contains N pairs (considering a and b) with a 'L' (means node b on left of a) or 'R' (means node b on right of a) after a and b.

Input:
2
2
1 2 L 1 3 R
5
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L

Output:
5
190
'''

# add data from left and right leaf nodes
def sumLeaf(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.data
    
    lsum = sumLeaf(root.left)
    rsum = sumLeaf(root.right)
    return lsum+rsum