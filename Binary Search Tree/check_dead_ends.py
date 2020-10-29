'''
https://practice.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1#
Given a Binary search Tree that contains positive integer values greater then 0. The task is to complete the function isDeadEnd which returns true if the BST contains a dead end else returns false. Here Dead End means, we are not able to insert any element after that node.
Examples:
Input :   
               8
             /   \ 
           5      9
         /  \     
        2    7 
       /
      1     
Output : Yes
Explanation : Node "1" is the dead End because after that we cant insert any element.       

Input :     
              8
            /   \ 
           7     10
         /      /   \
        2      9     13
Output : Yes
Explanation : We can't insert any element at node 9.  
'''

# method - 1
# save nodes in inorder to get sorted
# if node is leaf node and if i-1th node is 1 less and i+1th node is 1 more than current node than current node is dead end
def isdeadEnd(root):
    
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        arr.append(node)
        inorder(node.right)

    if root == None or ((not root.left) and (not root.right)):
        return False
    
    arr = []
    inorder(root)
    if arr[0].data == 1 and arr[1].data == 2:
        return True
        
    for i in range(1, len(arr)-1):
        if (not arr[i].left) and (not arr[i].right):
            if (arr[i].data - arr[i-1].data) == 1 and (arr[i+1].data - arr[i].data) == 1:
                return True
    
    return False

# method - 2 (recursively)
# use min - max concept, 
# if root is val then call on left (min, val-1) and right (val+1, max) in preorder
# ans is if min = max
def isdeadEnd(root):
    
    def checkdeadEnd(root, minval, maxval):
        if root == None:
            return False
        
        if minval == maxval:
            return True
        
        leftside = checkdeadEnd(root.left, minval, root.data-1)
        rightside = checkdeadEnd(root.right, root.data+1, maxval)
        return leftside or rightside
    
    return checkdeadEnd(root, 1, float('inf'))
    
    
    