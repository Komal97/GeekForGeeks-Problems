'''
https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1
Given a Binary Search Tree (with all values unique) and two node values. Find the Lowest Common Ancestors of the two nodes in the BST.
Input:
2
5 4 6 3 N N 7 N N N 8
7 8
2 1 3
1 3
Output:
7
2

Explanation:
Testcase1: The BST in above test case will look like
              5
           /     \ 
        4          6
     /     \     /    \
   3        N  N       7
 /    \              /    \ 
N   N               N     8
Here, the LCA of 7 and 8 is 7.
'''

# lca node always lie in range n1 and n2
# if n1 and n2 are less than root.data, move to left
# if n1 and n2 are greater than root.data, move to right
# otherwise root node is lca node
def LCA(root, n1, n2):
    
    if root == None:
        return None
    
    if n1<root.data and n2<root.data:
        return LCA(root.left, n1, n2)
    if n1>root.data and n2>root.data:
        return LCA(root.right, n1, n2)
    return root

# iterative - O(1) space
# if left and right condition doesnt satisfy
# means current node is lca, no need to traceback
def LCA(root, n1, n2):
    
    if root == None:
            return None

    node = root
    qval = n1
    pval = n2
    
    while node:
        parent = node.val
        if parent > pval and parent > qval:
            node = node.left
        elif parent < pval and parent < qval:
            node = node.right
        else:
            return node
    
    return None