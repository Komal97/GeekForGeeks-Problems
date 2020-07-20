'''
https://practice.geeksforgeeks.org/problems/merge-two-bst-s/1
Given two BST, Return elements of both BSTs in sorted form.
Expected Time Complexity: O(M+N) where M and N are the sizes if the two BSTs.
Expected Auxiliary Space: O(Height of BST1 + Height of BST2).
Input:
2
5 3 6 2 4
2 1 3 N N N 7 6
12 9 N 6 11
8 5 10 2

Output:
1 2 2 3 3 4 5 6 6 7
2 5 6 8 9 10 11 12
'''

# find inorder of 2 BST and return merged array of 2 BST
def inorder(root, out):
    if root == None:
        return
    inorder(root.left, out)
    out.append(root.data)
    inorder(root.right, out)
    
def merge(root1, root2):
    out1 = []
    out2 = []
    out = []
    inorder(root1, out1)
    inorder(root2, out2)
    
    i = 0
    j = 0
    while i < len(out1) and j < len(out2):
        if out1[i] < out2[j]:
            out.append(out1[i])
            i += 1
        else:
            out.append(out2[j])
            j += 1
    
    while i < len(out1):
        out.append(out1[i])
        i += 1
    while j < len(out2):
        out.append(out2[j])
        j += 1
    return out