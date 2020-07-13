'''
https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
Given two Binary Trees. Check whether they are Isomorphic or not.
Two trees are called isomorphic if one of them can be obtained from other by a series of flips, i.e. by swapping left and right children of a number of nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.
Input:
2
1 2 3 4
1 3 2 4
1 2 3 4
1 3 2 N N N 4
Output:
No
Yes
'''

# (left part of both trees and right part of both trees are equal) or (left and right of 2 trees and right and left of other side are equal)
def isIsomorphic(root1, root2): 
    if root1 == None and root2 == None:
        return True
    
    if root1 == None or root2 == None:
        return False
    
    if root1.data != root2.data:
        return False
    
    same = isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right)  
    cross = isIsomorphic(root1.left, root2.right) and isIsomorphic(root1.right, root2.left) 
    return same or cross