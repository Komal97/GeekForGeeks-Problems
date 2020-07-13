'''
https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1
Given a Binary Tree of size N , where each node has positive and negative values. Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

For example, the following tree

             10
          /      \
        -2        6
       /   \     /  \
     8     -4   7    5

should be changed to

       20(4-2+12+6)
          /       \
     4(8-4)      12(7+5)
       /   \         /  \
     0      0       0    0
Input:
2
3 1 2
10 20 30 40 60

Output:
0 3 0
0 100 0 150 0
'''
# if left and right are None then put data of root as 0 else sum of left and right
# always save data of root first then replace
def toSumTree(root) :
    def toSum(root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            temp = root.data
            root.data = 0
            return temp
        lsum = toSum(root.left)
        rsum = toSum(root.right)
        temp = root.data
        root.data = lsum + rsum
        return temp + root.data
        
    toSum(root)