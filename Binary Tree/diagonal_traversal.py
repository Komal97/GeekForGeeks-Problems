'''
https://www.interviewbit.com/problems/diagonal-traversal/
Given a Binary Tree A containing N nodes, return all diagonal elements in a binary tree belonging to same line.
Order does matter in the output. To get the same order as in the output traverse the tree same as we do in pre-order traversal.
Input 1:

            1
          /   \
         4      2
        / \      \
       8   5      3
          / \    /
         9   7  6
Input 2:

             11
          /     \
         20      12
        / \       \
       1   15      13
          /  \     /
         2    17  16
          \   /
          22 34


Example Output
Output 1:

 [1, 2, 3, 4, 5, 7, 6, 8, 9]
Output 2:

 [11, 12, 13, 20, 15, 17, 16, 1, 2, 22, 34]
'''

# to maintain preorder, use stack & for level order, use queue
# for left child -> d+1, for right child -> d same as that of root

class Solution:

    def solve(self, A):
        s = []
        if A == None:
            return s
        s.append((A, 0))
        h = {}
        
        while len(s)>0:
            node, d = s.pop()
            if d not in h:
                h[d] = []
            h[d].append(node.val)
            if node.right:
                s.append((node.right, d))
            if node.left:
                s.append((node.left, d+1))
        
        ans = []
        h = sorted(h.items(), key = lambda x: x[0])
        for d, nodelist in h:
            ans.extend(nodelist)
        return ans      