'''
https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
Given two binary trees, the task is to find if both of them are identical or not. 
Input:
3
1 2 3
1 2 3
1 2 3
1 3 2
1 2 3 N 3 N 10
1 2 3 N 3 N 10
Output:
Yes
No
Yes
'''

# identical when left is identical, right is identical and root data are equal
def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if (root1 == None and root2 != None) or (root1 != None and root2 == None):
        return False
    
    if root1.data != root2.data:
        return False
    
    left = isIdentical(root1.left, root2.left)
    right = isIdentical(root1.right, root2.right)

    return left and right
