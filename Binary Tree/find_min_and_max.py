'''
https://practice.geeksforgeeks.org/problems/max-and-min-element-in-binary-tree/1
Given a Binary Tree, find maximum and minimum elements in it.
Example:
Input:
1
7
2 7 L 2 5 R 7 6 R 6 1 L 6 11 R 5 9 R 9 4 L

Output:
11 1
'''
# find min/max from left, min/max from right
# return min/max among left, right and root
def findMax(root):
    if root == None:
        return float('-inf')
    
    lmax = findMax(root.left)
    rmax = findMax(root.right)
    return max(root.data, max(lmax, rmax))
    
def findMin(root):
    if root == None:
        return float('inf')
    
    lmin = findMin(root.left)
    rmin = findMin(root.right)
    return min(root.data, min(lmin, rmin))