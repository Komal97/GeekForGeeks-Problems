'''
https://practice.geeksforgeeks.org/problems/brothers-from-different-root/1#
Given two BSTs containing N1 and N2 distinct nodes respectively and given a value x. Your task is to complete the function countPairs(), that returns the count of all pairs from both the BSTs whose sum is equal to x.
Examples:
Input : BST 1:    5        
                /   \      
               3     7      
              / \   / \    
             2  4  6   8   

        BST 2:    10        
                /   \      
               6     15      
              / \   /  \    
             3  8  11  18
        x = 16
    
Output : 3
The pairs are: (5, 11), (6, 10) and (8, 8)
'''

# store inorder traversal of each BST in array
# use 2 pointer approach to find pairs
def countPairs(root1, root2, x):
    
    def inorder(root, arr):
        if root == None:
            return
        
        inorder(root.left, arr)
        arr.append(root.data)
        inorder(root.right, arr)
        
    bst1 = []
    bst2 = []
    inorder(root1, bst1)
    inorder(root2, bst2)
    
    count = 0
    i = 0
    j = len(bst2) - 1
    
    while i < len(bst1) and j >= 0:
        if bst1[i] + bst2[j] == x:
            count += 1
            i += 1
            j -= 1
        elif bst1[i] + bst2[j] < x:
            i += 1
        else:
            j -= 1
    return count


# use inorder on 1st BST and reverse inorder on 2nd BST iteratively (using stack)
# move like 2 pointer approach
def countPairs(root1, root2, x):
    
    count = 0
    stack1 = []
    stack2 = []
    
    cur = root1
    while cur:
        stack1.append(cur)
        cur = cur.left
    
    cur = root2
    while cur:
        stack2.append(cur)
        cur = cur.right
        
    while len(stack1) > 0 and len(stack2) > 0:
        if stack1[-1].data + stack2[-1].data == x:
            count += 1
            
            cur = stack1.pop().right
            while cur:
                stack1.append(cur)
                cur = cur.left
            
            cur = stack2.pop().left
            while cur:
                stack2.append(cur)
                cur = cur.right
        
        elif stack1[-1].data + stack2[-1].data < x:
            cur = stack1.pop().right
            while cur:
                stack1.append(cur)
                cur = cur.left
        
        else:
            cur = stack2.pop().left
            while cur:
                stack2.append(cur)
                cur = cur.right
    
    return count
            