'''
https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1
Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), that find the sum of all nodes on the longest path from root to leaf node.
If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

Examples:
Input : Binary tree:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output : 13

        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3 
      /
     6
sum = (4 + 2 + 1 + 6) = 13
'''

# keep global maxlevel and maxsum
# at leaf node, check if level > maxlevel, then update maxsum
def sumOfLongRootToLeafPath(root):
    
    maxsum = 0
    maxlevel = -1
    def longestPathSum(node, summ, level):
        nonlocal maxsum
        nonlocal maxlevel
        
        if node == None:
            return 
        
        if node.left == None and node.right == None:
            if level > maxlevel:
                maxsum = summ + node.data
                maxlevel = level
            elif level == maxlevel:
                maxsum = max(maxsum, summ + node.data)
            return
        
        
        longestPathSum(node.left, summ + node.data, level+1)
        longestPathSum(node.right, summ + node.data, level+1)
        
    longestPathSum(root, 0, 0)
    return maxsum
