'''
https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1
Given a Binary Tree having positive and negative nodes. Find the maximum sum of any level in the given Binary Tree.

Input :               4
                    /   \
                   2    -5
                  / \    /\
                -1   3 -2  6
Output: 6
Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 2'th level is 6
Hence maximum sum is 6

Input:
2
4 2 -5 -1 3 -2 6
1 2 3 4 5 N 8 N N N N 6 7
Output:
6
17
'''

# using level order, calculate sum of each level and find maximum
from collections import deque
def maxLevelSum(root):
    q = deque()
    q.append(root)
    
    maxsum = float('-inf')
    while len(q)>0:
        size = len(q)
        summ = 0
        for i in range(size):
            node = q.popleft()
            summ += node.data
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        maxsum = max(maxsum, summ)
    return maxsum