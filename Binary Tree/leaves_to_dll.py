'''
https://practice.geeksforgeeks.org/problems/leaves-to-dll/1
Given a Binary Tree, the task is to extract all leaves of it in a Doubly Linked List (DLL)in-place. 
In DLL, left means previous pointer and right means next pointer. 
Head of DLL should point to the leftmost leaf and then in inorder traversal and so on.
Input:

2
1 2 3
1 2 3 4

Output:

1
2 3
3 2
2 1
4 3
3 4

Explanation:
Testcase 2: After extracting leaves, 3 and 4 from the tree, the inorder traversal of the remaining binary tree produces 2, 1 and we have doubly linked list as 4 <-> 3.
'''

# use preorder, maintain prev
# if prev = None, means we reach first leaf node, then assign it to head 
# change left and right pointer of leaf nodes and change prev 
def leavesToDLL(root, head, prev):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        if prev[0] == None:
            head[0] = root
        else:
            prev[0].right = root
            root.left = prev[0]
        prev[0] = root
        return None
        
    root.left = leavesToDLL(root.left, head, prev)
    root.right = leavesToDLL(root.right, head, prev)
    return root
    
def convertToDLL(root):
    
    if root == None:
        return root
    
    head = [None]
    prev = [None]
    
    leavesToDLL(root, head, prev)
    
    return head[0]