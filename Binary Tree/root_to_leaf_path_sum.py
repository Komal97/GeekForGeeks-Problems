'''
https://practice.geeksforgeeks.org/problems/root-to-leaf-path-sum/1
Given a Binary Tree and a sum s, your task is to check whether there is a root to leaf path in that tree with the following sum .
Input
2
1 2 3
2
1 2 3
4

Output 
0
1

In above example there are two test case where each represents a tree with 3 nodes and 2 edges where root is 1, 
left child of 1 is 2 and right child of 1 is 3.  
'''

# reach child node and add root data to sum and then match this sum with the given sum
def hasPathSum(root, sm):
    def findpath(root, cur_sum, sm):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            cur_sum += root.data
            if cur_sum == sm:
                return 1
        left = findpath(root.left, cur_sum + root.data, sm)
        right = findpath(root.right, cur_sum + root.data, sm)
        return left or right
    return findpath(root, 0, sm)