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

# method - 1, hashing based solution using DFS(recursive) -> O(n) space
# method - 2, hashing based solution using BFS(iterative) -> levelorder ->  O(n)space
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

# method - 3 => logic is same of 2 pointer approach to find pair in sorted array
# do inorder traversal and inverse inorder traversal, do this iterative using stack - O(log n) space
class Solution:
       
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root == None or (root.left == None and root.right == None):
            return False
        
        leftinorder = []
        rightinorder = []
        
        leftptr = root
        rightptr = root
        
        while leftptr != None:
            leftinorder.append(leftptr)
            leftptr = leftptr.left
        
        while rightptr != None:
            rightinorder.append(rightptr)
            rightptr = rightptr.right
            
        while len(leftinorder) > 0 and len(rightinorder) > 0:
            
            if (leftinorder[-1].val + rightinorder[-1].val) == k and leftinorder[-1] != rightinorder[-1]:
                return True
            
            elif (leftinorder[-1].val + rightinorder[-1].val) < k:
                leftptr = leftinorder.pop()
                leftptr = leftptr.right
                while leftptr != None:
                    leftinorder.append(leftptr)
                    leftptr = leftptr.left
            else:
                rightptr = rightinorder.pop()
                rightptr = rightptr.left
                while rightptr != None:
                    rightinorder.append(rightptr)
                    rightptr = rightptr.right
        return False