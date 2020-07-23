'''
https://practice.geeksforgeeks.org/problems/median-of-bst/1
Given a Binary Search Tree, find the Median of its Node values.
Input:
2
6 3 8 1 4 7 9
6 3 8 1 4 7
Output:
6
5

Explanation:
Test Case 1: 
Given BST(with odd no. of nodes) is :
       6
     /   \
   3      8   
 /   \   /   \
 1   4   7   9
Inorder of Given BST will be : 1, 3, 4, 6, 7, 8, 9. So, here median will 6.
Test Case 2: 
Given BST(with odd no. of nodes) is :
       6
     /   \
   3      8   
 /   \    /   
1    4   7   
Inorder of Given BST will be : 1, 3, 4, 6, 7, 8. So, here median will (4 + 6)/2 = 10/2 = 5.
'''

# store values in arr and return median
def inorder(root, arr):
    if root == None:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)
    
def findMedian(root):
    
    arr = []
    inorder(root, arr)
    n = len(arr)
    if n&1:
        return arr[n//2]
    
    val = arr[(n-1)//2] + arr[n//2]
    if val&1:
        return val/2
    return val//2