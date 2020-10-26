'''
https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1
Given a Binary Tree, check if all leaves are at same level or not.
Example 1:
Input: 
            1
          /   \
         2     3

Output: 1
Explanation: 
Leaves 2 and 3 are at same level.

Example 2:
Input:
            10
          /    \
        20      30
       /  \        
     10    15
Output: 0
Explanation:
Leaves 10, 15 and 30 are not at same level.
'''

# save leaf level and check each leaf level with the saved leaf level
def check(node):
    
    def checkLeafLevel(node, leaflevel, level):
        if node == None:
            return True
    
        if node.left == None and node.right == None:
            if leaflevel[0] == -1 or  level == leaflevel[0]:
                leaflevel[0] = level
                return True
            elif level != leaflevel[0]:
                return False
                
        left = checkLeafLevel(node.left, leaflevel, level+1)
        right = checkLeafLevel(node.right, leaflevel, level+1)
        return left and right
    
    leaflevel = [-1]
    return checkLeafLevel(node, leaflevel, 0)
        

# iterative using level order
from collections import deque
def check(node):
    
    q = deque([node])
    
    leaflevel = -1
    level = 0
    
    while len(q):
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if not node.left and not node.right:
                if leaflevel == -1:
                    leaflevel = level
                elif leaflevel != level:
                    return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        level += 1
    
    return True