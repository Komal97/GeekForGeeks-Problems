'''
https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
Given a binary tree, connect the nodes that are at same level. You'll be given an addition nextRight pointer for the same.
Input:
2
3 1 2
10 20 30 40 60
Output:
3 1 2
1 3 2
10 20 30 40 60
40 20 60 10 30

Explanation:
Testcase1: The connected tree is
        3 ------> NULL
     /      \
   1 -----> 2 ------ NULL
Testcase2: The connected tree is
                           10 ----------> NULL
                        /      \
                     20 ------> 30 -------> NULL
                  /       \
                 40 ----> 60 ----------> NULL
'''

# method - 1 => using level order
# connect 'nextRight' pointer of each node to next node at same level
from collections import deque
def connect(root):
    
    if root == None:
        return
    
    q = deque()
    q.append(root)
    
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i==size-1:
                node.nextRight = None
            else:
                node.nextRight = q[0]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
# method - 2 => preorder - set root first, root.left.next = root.right and root.right = root.next.left
def connect(root):
    
    if root == None:
        return
    
    root.next = None
    def connectNext(root):
        if root == None:
            return
    
        if root.left:
            root.left.next = root.right

        if root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None

        connectNext(root.left)
        connectNext(root.right)
        
    connectNext(root)
    return root