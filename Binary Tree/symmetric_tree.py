'''
https://practice.geeksforgeeks.org/problems/symmetric-tree/1
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).
Input:
3
5 1 1 2 N N 2
5 10 20 20 20 N 30
100 10 10 20 20 20 20
Output:
True
False
True
Explanation:
TestCase 1:

             5
           /   \
          1     1
         /       \
        2         2
Tree is mirror image of itself i.e. tree is symmetric

TestCase 2:

            5
          /    \
        10      20
      /    \      \
    20     20      30 
Tree is not mirror image of itself i.e. tree is not symmetric
'''

# check tree is mirror image of itself 
# or check mirror image for left tree and right tree
def areMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
   
    if root1 and root2 and root1.data == root2.data:
        left = areMirror(root1.left, root2.right) 
        right = areMirror(root1.right, root2.left)
        return left and right

    return False
        
def isSymmetric(root):
    if root == None:
        return True
    return areMirror(root.left, root.right)

# iterative
def checkSymmetric(root1, root2):
        
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False

    stack1 = [root1]
    stack2 = [root2]

    while len(stack1) and len(stack2):
        node1 = stack1.pop()
        node2 = stack2.pop()
        
        if node1 == None and node2 == None:
            continue
        if node1 == None or node2 == None:
            return False
        if node1.val != node2.val:
            return False
        stack1.append(node1.left)
        stack2.append(node2.right)
        stack1.append(node1.right)
        stack2.append(node2.left)
    return True

def isSymmetric(root: TreeNode):
    if root == None:
        return True
    return checkSymmetric(root.left, root.right)