'''
https://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree-single-traversal/
Given a binary tree and a node, print all cousins of given node. Note that siblings should not be printed.

Examples:
Input 1:
A =       1
         /   \
        2     3
       / \   / \
      4   5 6   7 
B = 5
Output: [6, 7]

Input 2:
A =         1
          /   \
         2     3
        / \ .   \
       4   5 .   6
B = 1
Output: []
'''

# use level order
# push in queue until we found node
# if left or right or a parent is search find, then flag=True and dont push siblings and push all other nodes at same level
# now queue has elements without siblings of required level
from collections import deque
class Solution:
    def solve(self, A, B):
        if not A or A.val == B:
            return []
        
        found = False
        q = deque()
        q.append(A)
        ans = []
        while len(q) > 0 and found==False:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if (node.left and node.left.val == B) or (node.right and node.right.val == B):
                    found=True
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        if found:
            while len(q) > 0:
                ans.append(q.popleft().val)
                
        return ans   
        