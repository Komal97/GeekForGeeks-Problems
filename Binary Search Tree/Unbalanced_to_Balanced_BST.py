'''
https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1
Given a Binary Search Tree of size N, that may be unbalanced. Your task is to complete the function buildBalancedTree(), that convert the given BST into a balanced BST that has minimum possible height.
Input:
2
3
30 20 10
5
10 8 7 6 5
Output:
2
3

Explanation:
Input:
         4
        /
       3
      /
     2
    /
   1
Output:
      3            3           2
    /  \         /  \        /  \
   1    4   OR  2    4  OR  1    3   OR ..
    \          /                   \
     2        1                     4 
'''

# use inorder traversal and store elements in array which is sorted - O(n)
# build BST from sorted array by taking mid as root, its left part as left tree and right part as right tree - O(n)
# time complexity: O(n+n) = O(n)
def inorder(root, traversal_out):
    if root == None:
        return
    inorder(root.left, traversal_out)
    traversal_out.append(root.data)
    inorder(root.right, traversal_out)

def sortedArrayToBST(s, e, arr):
    if s>e:
        return None
    
    mid = (s+e)//2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(s, mid-1, arr)
    root.right = sortedArrayToBST(mid+1, e, arr)
    return root
    
def buildBalancedTree(root): 
    
    traversal_out = []
    inorder(root, traversal_out)
    root = sortedArrayToBST(0, len(traversal_out)-1, traversal_out)
    return root
