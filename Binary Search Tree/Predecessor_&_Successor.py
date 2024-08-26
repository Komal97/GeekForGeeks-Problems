'''
https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1
There is BST given with root node with key part as integer only. You need to find the inorder successor and predecessor of a given key. In case, if the either of predecessor or successor is not found print -1.
Input:
2
6
50 30 L 30 20 L 30 40 R 50 70 R 70 60 L 70 80 R
65
6
50 30 L 30 20 L 30 40 R 50 70 R 70 60 L 70 80 R
100

Output:
60 70
80 -1
'''

# assign value to predecessor until root->data < key 
# assign value to successor if it is null and just greater than given key and return
class Solution:
    def findPreSuc(self, root, pre, suc, key):
    
        pred = [None]
        succ = [None]
        def find(node):
            if not node:
                return
            
            find(node.left)
            
            if node.key < key:
                pred[0] = node
                
            elif not succ[0] and node.key > key:
                succ[0] = node
                return
            
            find(node.right)
            
        find(root)
        if pred[0] != None:
            pre.key = pred[0].key
        if succ[0] != None: 
            suc.key = succ[0].key