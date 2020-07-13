'''
https://practice.geeksforgeeks.org/problems/construct-tree-1/1
Given 2 Arrays of Inorder and preorder traversal. Construct a tree and print the Postorder traversal. 
Input:
2
4
1 6 8 7
1 6 7 8
6
3 1 4 0 5 2
0 1 3 4 2 5

Output:
8 7 6 1
3 4 1 5 2 0

Explanation:
Test Case 2: Tree constructed from given traversals will be:
            0
         /      \
        1         2
      /     \     /
     3       4   5
'''

def construct(pre, pre_s, pre_e, inor, in_s, in_e):
    # base case
    if pre_s>pre_e or in_s>in_e:
        return None
    
    # first node in preorder is root node
    n = Node(pre[pre_s])
    
    # find that node in inorder 
    ind = -1
    for i in range(in_s, in_e+1):
        if inor[i] == pre[pre_s]:
            ind = i
            break
        
    # left part of ind is left tree and right part is right tree in inorder
    # find indexes of left and right part in preorder also
    next_ind_pre = ind-in_s   # number of left elements
    n.left = construct(pre, pre_s+1, pre_s+next_ind_pre, inor, in_s, ind-1)
    n.right = construct(pre, pre_s+next_ind_pre+1, pre_e, inor, ind+1, in_e)
    return n
    
    
def buildtree(inorder, preorder, n):
    root = construct(preorder, 0, n-1, inorder, 0, n-1)
    return root
