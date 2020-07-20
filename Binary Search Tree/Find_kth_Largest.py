'''
https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1
Given a Binary search tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.
Expected Time Complexity: O(H + K).
Expected Auxiliary Space: O(H).
Input:
2
4 2 9 1 3 N 10
3
9 N 10
1
Output:
4
10
'''
# method - 1 O(n) time, O(n) space, inorder traversal gives sorted elements so store them and return value from last - 
def inorder(root, arr):
    if root == None:
        return
    
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)
    
def kthLargest(root, k):
    
    arr = []
    inorder(root, arr)
    if len(arr) < k:
        return -1
    return arr[len(arr)-k]


# method - 2 O(h+k), O(h) space, reverse inorder traversal to right then increment count until count != k and then left
def inorder(root, k, c):
    if root == None or c[0] >= k:
        return 
    inorder(root.right, k, c)
    c[0] += 1
    if c[0] == k:
        c[1] = root.data
        return
    inorder(root.left, k, c)
    
    
def kthLargest(root, k):
    
    c = [0, -1]
    inorder(root, k, c)
    
    return c[1]