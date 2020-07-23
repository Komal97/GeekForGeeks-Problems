'''
https://practice.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1
Given a Binary Search Tree and a target sum. Check whether there's a pair of Nodes in the BST with value summing up to the target sum. 
Input:
2
2 1 3
5
6 5 N 3 N 1 4
2
Output:
1
0
'''

# method - 1, hashing based solution
def isPairPresent(root, target): 
    
    m = {}
    def check(root, target):
        nonlocal m
        if root == None:
            return False
        
        if target-root.data in m:
            return True
            
        m[root.data] = root
        left = check(root.left, target)
        right = check(root.right, target)
        return left or right
    return int(check(root, target))