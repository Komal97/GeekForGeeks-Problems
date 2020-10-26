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

# find LCA using recursion
# then return of depth of node 1 from lCA  + depth of node 2 from lCA
def findLCA(node, A, B):
    if node == None:
        return None
    
    if node.data == A or node.data == B:
        return node
        
    l = findLCA(node.left, A, B)
    r = findLCA(node.right, A, B)
    
    if l and r:
        return node
    
    return l if l else r

def findLevel(node, d, level, searchnode):
    if node == None:
        return
    
    if node.data == searchnode:
        d.append(level)
        return 
    
    findLevel(node.left, d, level+1, searchnode)
    findLevel(node.right, d, level+1, searchnode)
    
def findDist(root,a,b):
    
    lca = findLCA(root, a, b)
    
    d1 = []
    d2 = []
    
    findLevel(lca, d1, 0, a)
    findLevel(lca, d2, 0, b)

    if len(d1) > 0 and len(d2) > 0:
        return d1[0] + d2[0]
    
    return -1