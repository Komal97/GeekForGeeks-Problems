'''
https://practice.geeksforgeeks.org/problems/add-all-greater-values-to-every-node-in-a-bst/1
Given a BST, modify it so that all greater values in the given BST are added to every node.
Input:
2
50 30 70 20 40 60 80
2 1 5 N N 4 7

Output:
350 330 300 260 210 150 80
19 18 16 12 7
Explanation:

              50
           /      \
         30        70
        /   \      /  \
      20    40    60   80 

The above tree should be modified to following 

              260
           /      \
         330        150
        /   \       /  \
      350   300    210   80
'''

# use reverse inorder traversal(right, root, left), and replace root.data with sum + root.data
def modify(root):
    
    if root == None:
        return None
        
    def changeData(root):
        nonlocal summ
        if root == None:
            return
        
        changeData(root.right)
        root.data += summ
        summ = root.data
        changeData(root.left)
        
    summ = 0
    changeData(root)
    return root 