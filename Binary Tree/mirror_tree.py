'''
https://practice.geeksforgeeks.org/problems/mirror-tree/1
Given a Binary Tree, convert it into its mirror.
Input:
2
1 3 2
10 20 30 40 60
Output:
2 1 3
30 10 60 20 40

Explanation:
Testcase1: The tree is
        1         (mirror)         1
     /      \         =>        /     \
   3       2                  2         3
The inorder of mirror is 2 1 3
Testcase2: The tree is
                           10                                 10
                        /     \           (mirror)         /      \
                     20         30            =>        30        20
                  /       \                                     /    \
               40       60                                      60    40
The inroder traversal of mirror is 30 10 60 20 40.
'''

# swap left and right pointers and call for rest tree
def mirror(root):
    if root == None:
        return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

# swap left and right while popping from queue
from collections import deque
def mirror(root):
   
   q = deque([root])
   
   while len(q):
      node = q.popleft()
      node.left, node.right = node.right, node.left
      if node.left:
            q.append(node.left)
      if node.right:
            q.append(node.right)
            
            
   return root