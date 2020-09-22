'''
https://practice.geeksforgeeks.org/problems/height-of-spiral-tree/1
Given a special Binary Tree whose leaf nodes are connected to form a circular doubly linked list. Find the height of this special Binary Tree.
Example 1:
Input:
        1
      /   \
     2     3
    / \
   4   5
  /
 6
Output: 4
​Explanation: 
In the above binary tree, 6, 5 and 3 are leaf nodes and they form a circular doubly linked list. Here, the left pointer of leaf node will act as a previous pointer of circular doubly linked list and its right pointer will act as next pointer of circular doubly linked list.
'''

# method - 1 => create visited array, and using BFS find total level
from collections import deque, defaultdict
def findTreeHeight(root):
    
    q = deque([root])
    level = 0
    visited = defaultdict(bool)
    visited[root] = True
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left and not visited[node.left]:
                q.append(node.left)
                visited[node.left] = True
            if node.right and not visited[node.right]:
                q.append(node.right)
                visited[node.right] = True
        level += 1
    return level

# method - 2 => check circular conditions extra
# if current node is equal to next node's previous or next 
def findTreeHeight(root):
    
    if root == None:
        return 0
    
    if (root.left != None and root == root.left.right) or (root.right != None and root == root.right.left):
        return 1
    
    lh = findTreeHeight(root.left)
    rh = findTreeHeight(root.right)
    
    return max(lh, rh) + 1