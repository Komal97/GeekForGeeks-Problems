'''
https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
Write a function to print Boundary Traversal of a binary tree. Boundary Traversal of a binary tree here means that you have to print boundary nodes of the binary tree Anti-Clockwise starting from the root.
Input:
2
1 2 3
10 20 30 40 60

Output:
1 2 3
10 20 40 60 30
'''

# handle root node separately                                                        _
# traverse left nodes except leaf
# traverse leaf nodes
# traverse right nodes except leaf
def leftnodes(root, ans):
    if root == None:
        return
    
    # move towards leftmost nodes
    if root.left != None:
        ans.append(root.data)
        leftnodes(root.left, ans)
    # move towards right node if left node don't exist on left side
    elif root.right != None:
        ans.append(root.data)
        leftnodes(root.right, ans)
    # else do nothing because leaf node come
    
def leafnodes(root, ans):
    if root == None:
        return
    if root.left == None and root.right == None:
        ans.append(root.data)
        return
    
    leafnodes(root.left, ans)
    leafnodes(root.right, ans)
    

def rightnodes(root, ans):
    if root == None:
        return
    
    # move towards rightmost nodes
    if root.right != None:
        rightnodes(root.right, ans)
        ans.append(root.data)
    # move towards left node if right node don't exist on right side
    elif root.left != None:
        rightnodes(root.left, ans)
        ans.append(root.data)
    # else do nothing because leaf node come
    
def printBoundaryView(root):
    ans = []
    ans.append(root.data)
    leftnodes(root.left, ans)
    leafnodes(root.left, ans)
    leafnodes(root.right, ans)
    rightnodes(root.right, ans)
    return ans