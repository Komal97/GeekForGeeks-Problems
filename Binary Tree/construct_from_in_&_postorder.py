'''
https://practice.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1
Given inorder and postorder traversals of a Binary Tree in the arrays in[] and post[] respectively. The task is to construct the binary tree from these traversals.
Input:
2
8
4 8 2 5 1 6 3 7
8 4 5 2 6 7 3 1
5
9 5 2 3 4
5 9 3 4 2
Output:
1 2 4 8 5 3 6 7
2 9 5 4 3

Explanation:
Testcase 1: For the given postorder and inorder traversal of tree the  resultant binary tree will be
          1
       /     \
     2        3
   /    \   /   \
  4     5   6    7
    \
      8
Testcase 2: For the given postorder and inorder traversal of tree the  resultant binary tree will be
            2
          /    \
        9       5
      /   \
    4      3
'''

def construct(post, post_s, post_e, In, in_s, in_e):
    # base case
    if post_s>post_e or in_s>in_e:
        return None
    
    # last node in postorder is root node
    n = Node(post[post_e])
    
    # find that node in inorder
    ind = -1
    for i in range(in_s, in_e+1):
        if In[i] == post[post_e]:
            ind = i
            break
    
    # left part of ind is left tree and right part is right tree in inorder
    # find indexes of left and right part in postorder also
    nre = in_e-ind  # number of right elements
    n.left = construct(post, post_s, post_e - nre - 1, In, in_s, ind-1)
    n.right = construct(post, post_e - nre, post_e-1, In, ind+1, in_e)
    return n
    
def buildTree(In, post, n):
    
   root = construct(post, 0, n-1, In, 0, n-1)
   return root