'''
https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /    \   /    \
  4     5   6    7
   \
     8   

Input:
2
1 3 2
10 20 30 40 60 N N
Output:
1 3
10 20 40
'''
# use level order 
# LEFT VIEW - first node of each level constitute left view
from collections import deque
def LeftView(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i==0:
                print(node.data, end = " ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

'''
https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

        1
       /     \
     2        3
   /   \    /    \
  4     5   6    7
    \
     8
'''    
# RIGHT VIEW - last node of each level consitute right view              
from collections import deque
def rightView(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i==size-1:
                print(node.data, end = " ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
