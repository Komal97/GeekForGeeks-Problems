'''
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Input:
2
2
1 2 L 1 3 R
6
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L 30 100 R

Output:
2 1 3
40 20 10 30 100

Explanation:
Test case 2:

            10

         /    \

     20        30

   /      \  /     \

40      60 90     100

TopView is: 40 20 10 30 100
'''

# use vertical order print
# TOP VIEW - first node of every line constitute top view
from collections import deque
def topView(root):
    
    if root == None:
        return
    q = deque()
    q.append((root, 0))
    h = {}
    
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node, k = q.popleft()
            if k not in h:
                h[k] = []
            h[k].append(node.data)
            if node.left:
                q.append((node.left, k-1))
            if node.right:
                q.append((node.right, k+1))
    h = sorted(h.items(), key = lambda x: x[0])

    for dist, nodelist in h:
        print(nodelist[0], end = " ")
        

'''
https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
Input:
2
1 3 2
10 20 30 40 60
Output:
3 1 2
40 20 60 30
'''

# use vertical order print
# BOTTOM VIEW - last node of every line constitute top view
from collections import deque
def bottomView(root):
    q = deque()
    q.append((root, 0))
    h = {}
    
    while len(q)>0:
        size = len(q)
        for i in range(size):
            node, k = q.popleft()
            if k not in h:
                h[k] = []
            h[k].append(node.data)
            if node.left:
                q.append((node.left, k-1))
            if node.right:
                q.append((node.right, k+1))

    h = sorted(h.items(), key = lambda x: x[0])
    ans = []
    for dist, nodelist in h:
        ans.append(nodelist[len(nodelist)-1])
    return ans