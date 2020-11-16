'''
https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/
Given a binary tree, task is to find subtree with maximum sum in tree.

Examples:

Input :       1
            /   \
           2      3
          / \    / \
         4   5  6   7
Output : 28
As all the tree elements are positive,
the largest subtree sum is equal to
sum of all tree elements.

Input :       1
            /    \
          -2      3
          / \    /  \
         4   5  -6   2
Output : 7
Subtree with largest sum is :  -2
                             /  \ 
                            4    5
Also, entire tree sum is also 7.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# build binary tree
def buildTree():
    data = int(input())
    if data == -1:
        return None
    n = Node(data)
    n.left = buildTree()
    n.right = buildTree()
    return n

class Pair():
    def __init__(self):
        self.summ = 0
        self.maxsumm = 0

def findLargestSubtreeSum(root):
    p = Pair()
    if not root:
        return p 
    
    lpair = findLargestSubtreeSum(root.left)
    rpair = findLargestSubtreeSum(root.right)

    p.summ = lpair.summ + rpair.summ + root.data
    p.maxsumm = max(lpair.maxsumm, rpair.maxsumm, p.summ)
    return p 

root = buildTree()
maxsumm = findLargestSubtreeSum(root)
print(maxsumm.maxsumm)