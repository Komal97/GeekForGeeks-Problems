'''
https://practice.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1
Given a BST and an integer K. Find the Kth Smallest element in the BST. 
Input:
2
2 1 3
2
2 1 3
5
Output:
2
-1
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# inorder traversal - elements are sorted
# find node in left subtree then current node then right subtree
def smallest(root, c, k):
    # base condition
    if root == None:
        return None
    
    # if kth smallest node is present in left subtree
    left = smallest(root.left, c, k)
    if left:
        return left
    
    # if current node is kth smallest
    c[0] += 1
    if c[0] == k:
        return root
    
    # else find element in right subtree
    return smallest(root.right, c, k)
    
def KthSmallestElement(root, K): 
    if root == None:
        return -1
    c = [0]
    temp = smallest(root, c, K)
    return temp.data if temp else -1