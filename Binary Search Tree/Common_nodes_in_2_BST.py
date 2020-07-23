'''
https://practice.geeksforgeeks.org/problems/print-common-nodes-in-bst/1
Given two Binary Search Trees(without duplicates). Find need to print the common nodes in them. In other words, find intersection of two BSTs
Input:
2
5 1 10 0 4 7 N N N N N N 9
10 7 20 4 9
10 2 11 1 3
2 1 3
Output:
4 7 9 10
1 2 3
'''

# inorder traversal of 2 BST and store in diff arrays
# find intersection of 2 arrays which are sorted
def inorder(root, ans):
    if root == None:
        return
    inorder(root.left, ans)
    ans.append(root.data)
    inorder(root.right, ans)
    
def printCommon(root1, root2):
    
    ans = []
    if root1 == None or root2 == None:
        return ans
    tree1 = []
    tree2 = []
    inorder(root1, tree1)
    inorder(root2, tree2)
    
    i = 0
    j = 0
    while i < len(tree1) and j < len(tree2):
        if tree1[i] == tree2[j]:
            ans.append(tree1[i])
            i += 1
            j += 1
        elif tree1[i] < tree2[j]:
            i += 1
        else:
            j += 1
    return ans