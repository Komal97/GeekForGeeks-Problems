'''
https://practice.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1
Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Expected Time Complexity : O(n)

Expected Auxiliary Space : O(1)

Constraints:
1 <= T <= 1000
1 <= N <= 1000

Example:
Input:
2
10 5 8 2 20 (20 and 8 should be replaced)
11 3 17 N 4 10 (11 and 10 should be replaced)

Output:
1
1
'''

# use inorder traversal because keys are sorted, keep reference of prev, first, last node
# in swapped tree, in inorder traversal -> 2 5 20 10 8, 20>10 so 20 and 10>8 so 8 will be replaced (prev > root)
# when we return or go right, then only update prv
def correctBST(root):
    
    if root == None:
        return None
        
    def findNodes(root, prev_node, first, second): cxdswq   
        if root == None:
            return
        
        # keep moving left
        findNodes(root.left, prev_node, first, second)
        # check if prv is greater (20>10) then prev is first incorrect node
        if prev_node[0] and prev_node[0].data > root.data:
            # first node of first pair and second node of second pair is incorrect
            if first[0] == None:
                first[0] = prev_node[0]
            second[0] = root
        # update prv node 
        prev_node[0] = root
        findNodes(root.right, prev_node, first, second)
        
    
    first = [None]
    second = [None]
    prev_node = [None]
    findNodes(root, prev_node, first, second)
    first[0].data, second[0].data = second[0].data, first[0].data
    return root