'''
https://practice.geeksforgeeks.org/problems/duplicate-subtrees/1#
Given a binary tree of size N, your task is to complete the function printAllDups(), that finds and prints all duplicate subtrees from the given binary tree.
For each duplicate subtrees, you only need to print the root node value of any one of them.
Two trees are duplicate if they have the same structure with same node values.
Example:

Input : 
    1
   /  \
  2    3
 /    / \
4    2   4
    /
   4
Output : 2-4 and 4
Explanation: Above Trees are two duplicate subtrees. Therefore, you need to return above trees root in the form of a list.
'''

# save subtree string in map (left, root, right)
# and check in postorder whether it is occuring again
from collections import defaultdict
def printAllDups(root):
    
    freq = defaultdict(int)
    ans = []
    
    def findDuplicate(node):
 
        if not node:
            return ''
        
        exp = '('
        exp += findDuplicate(node.left)
        exp += str(node.data)
        exp += findDuplicate(node.right)
        exp += ')'
        
        if exp in freq and freq[exp] == 1:
            ans.append(node.data)
        
        freq[exp] += 1
        
        return exp
    
    findDuplicate(root)
    if len(ans) > 0:
        print(*sorted(ans), sep = ' ' , end = ' ')
    else:
        print(-1, end = ' ')