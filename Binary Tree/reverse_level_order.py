'''
https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1
Given a Binary Tree of size N. You have to print the Reverse Level Order Traversal of the given tree.
Input:
2
1 3 2
10 20 30 40 60

Output:
3 2 1
40 60 20 30 10

TestCase 1:
    1
  /   \
 3     2    
'''

# same as that of level order
# first push right node and then left node
# store ans in an array/stack and print reversed array/stack
from collections import deque
def reversePrint(root):
    if root == None:
        return
    
    stack = []
    q = deque()
    q.append(root)
    
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            stack.append(node.data)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
    while len(stack)>0:
        print(stack.pop(), end = ' ')