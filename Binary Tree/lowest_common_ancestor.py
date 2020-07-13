'''
https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1
Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. 
We may assume that either both n1 and n2 are present in the tree or none of them is present. 
Input:
2
2 3
1 2 3
3 4
5 2 N 3 4
Output:
1
2

Explanation:
Testcase1: The tree is
        1
     /      \
   2        3
The LCA of 2 and 3 is 1.
Testcase 2: The tree is
          5
        /
      2
     /   \
   3     4
The lowest common ancestor of given nodes 3 and 4 is 2.
'''

# we find node to root path for both given nodes
# then we start matching path from last in array or top of tree and break where we get unequal data
def nodeToRoot(root, data, path):
    if root == None:
        return False
    
    if root.data == data:
        path.append(root)
        return True
    
    left = nodeToRoot(root.left, data, path)
    if left:
        path.append(root)
        return True
    
    right = nodeToRoot(root.right, data, path)
    if right:
        path.append(root)
        return True
    
    return False
    
def lca(root, n1, n2):
    path1 = []
    path2 = []
    nodeToRoot(root, n1, path1)
    nodeToRoot(root, n2, path2)
    
    i = len(path1)-1
    j = len(path2)-1

    while i>=0 and j>=0 and path1[i].data == path2[j].data:
        i -= 1
        j -= 1
    
    if i<len(path1)-1: i += 1
    if j<len(path2)-1: j += 1
    return path1[i]
