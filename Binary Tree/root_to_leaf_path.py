'''
https://practice.geeksforgeeks.org/problems/root-to-leaf-paths/1
Given a Binary Tree of size N, you need to find all the possible paths from root node to all the leaf node's of the binary tree.

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
All possible paths:
1->2->4
1->2->5
1->3->6
1->3->7
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree.

Example:
Input:
2
1 2 3
10 20 30 40 60
Output:
1 2 #1 3 #
10 20 40 #10 20 60 #10 30 #
'''

# when we reach leaf node then we print print path, at each point string containing path to that level only
def printPath(root):
    
    def findpath(root, path):
        if root == None:
            return 
        if root.left == None and root.right == None:
            path += str(root.data)
            print(path, end = ' #')
            return
        findpath(root.left, path + str(root.data) + " ")
        findpath(root.right, path + str(root.data) + " ")
        
    findpath(root, "")