'''
https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1
Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
Sample Input:
3
1 2 3 4 
1 3 2
10 20 30 40 60

Output:
1 2 3 4 
1 2 3
10 20 30 40 60

Explanation:
Testcase 1 : The binary tree is 

          1
        /   \
       2     3
      /        
     4       

The converted BST will be

        3
      /   \
    2      4
   /
  1
'''
# structure of tree should remain same but data should be according to BST
# store elements of binary tree using inorder traversal in arr
# sort the arr
# now put elements in binary tree in inorder traversal
def inorderBinary(root, arr):
    if root == None:
        return
    
    inorderBinary(root.left, arr)
    arr.append(root.data)
    inorderBinary(root.right, arr)
    
def copyElements(root, arr, i):
    if root == None:
        return
    
    copyElements(root.left, arr, i)
    root.data = arr[i[0]]
    i[0] += 1
    copyElements(root.right, arr, i)
    
def binaryTreeToBST(root):
    if root == None:
        return
    
    arr = []
    inorderBinary(root, arr)
    arr.sort()
    i = [0]
    copyElements(root, arr, i)
    
