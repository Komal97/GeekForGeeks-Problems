'''
https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1#
Given a binary tree of size  N, a node and a positive integer K., your task is to complete the function kthAncestor(), 
the function should return the Kth ancestor of the given node in the binary tree. If there does not exist any such ancestor then return -1.
Input: 
        1
     /    \
    2      3
  /   \
 4     5
K = 2, Node = 4 
Output: 1
Since, K is 2 and node is 4, so we first need to locate the node and look k times its ancestors.
Here in this Case node 4 has 1 as his 2nd Ancestor aka the Root of the tree.
'''
# search node, trace back and find node k far from the node, keep global variable
def kthAncestor(root,k, node):
    
    kth = [k]
    ans = [None]
    
    def findKthAncestor(root):
        
        if root == None:
            return False
        
        if root.data == node:
            return True
        
        left = findKthAncestor(root.left)
        if left:
            kth[0] -= 1
            if kth[0] == 0 and ans[0] == None:
                ans[0] = root
            return True
            
        right = findKthAncestor(root.right)
        if right:
            kth[0] -= 1
            if kth[0] == 0 and ans[0] == None:
                ans[0] = root
            return True
        
        return False
        
    check = findKthAncestor(root)
    if ans[0] == None:
        return -1

    return ans[0].data
