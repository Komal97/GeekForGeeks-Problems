'''
https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1
Given a binary tree and two node values your task is to find the minimum distance between them.
Input
1
2
1 2 3
2 3 

Output
2

Explanation:
Test Case 1: The tree formed is:
      1
     /  \ 
   2     3
We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2. 
'''

# find lowest common ancestor because only after that path of both nodes will diverge
# return i+j because i is i distance away from a and same with b
def nodeToRootPath(root, data, path):
    if root == None:
        return False
    
    if root.data == data:
        path.append(root.data)
        return True
        
    left = nodeToRootPath(root.left, data, path)
    if left:
        path.append(root.data)
        return True
    
    right = nodeToRootPath(root.right, data, path)
    if right:
        path.append(root.data)
        return True
    return False
    
def findDist(root,a,b):
    
    path1 = []
    path2 = []
    nodeToRootPath(root, a, path1)
    nodeToRootPath(root, b, path2)
    i = len(path1) - 1
    j = len(path2) - 1
    
    while i>=0 and j>=0 and path1[i] == path2[j]:
        i-=1
        j-=1
    
    if i<len(path1)-1: i+= 1
    if j<len(path2)-1: j+= 1
    
    return i+j