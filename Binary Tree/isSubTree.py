'''
https://practice.geeksforgeeks.org/problems/check-if-subtree/1
Given two binary trees with head reference as T and S having at most N nodes. The task is to check if S is present as subtree in T.
Input:
3
1 2 3 N N 4
3 4
26 10 N 20 30 40 60
26 10 N 20 30 40 60
26 10 3 4 6 N 3 N N N 25
10 4 6 N 30
Output:
1
1
0

Explanation:
Testcase 1: Given trees are 
T:                   1                                  S:                  3
                   /    \                                                 /
                 2       3                                               4
               /    \    /   
             N    N  4
S is the subtree in T.
'''

# method - 1 -> O(n^2)
# check if T1 and T2 are identical, if not then check left and right subtree
def identical(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if root1 and root2 and root1.data == root2.data:
        left = identical(root1.left, root2.left)
        right = identical(root1.right, root2.right)
        return left and right
    return False
    
def isSubTree(T1, T2):
    if T1 == None and T2 == None:
        return True
    if T1 == None or T2 == None:
        return False
    
    if T1.data == T2.data and identical(T1, T2):
        return True
            
    left = isSubTree(T1.left, T2)
    right = isSubTree(T1.right, T2)
  
    return left or right


# method - 2 -> O(n)
# two trees are identical if their inorder and preorder/postorder are same
def preorder(root, output):
    if root == None:
        output.append('$')
        return
    
    output.append(str(root.data))
    preorder(root.left, output)
    preorder(root.right, output)

def inorder(root, output):
    if root == None:
        output.append('$')
        return
    
    inorder(root.left, output)
    output.append(str(root.data))
    inorder(root.right, output)
    
def isSubTree(T1, T2):
    if T1 == None and T2 == None:
        return True
    if T1 == None or T2 == None:
        return False
    
    preoutT1 = []
    preoutT2 = []
    preorder(T1, preoutT1)
    preorder(T2, preoutT2)
    preoutT1 = ' '.join(preoutT1)
    preoutT2 = ' '.join(preoutT2)
    if preoutT2 not in preoutT1:
        return False
    
    inoutT1 = []
    inoutT2 = []
    inorder(T1, inoutT1)
    inorder(T2, inoutT2)
    inoutT1 = ' '.join(inoutT1)
    inoutT2 = ' '.join(inoutT2)
    return inoutT2 in inoutT1