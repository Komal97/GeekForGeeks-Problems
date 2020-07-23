'''
https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1
Given a BST,  and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.
Input:
2
20 8 22 4 12 N N N N 10 14
8
20 8 22 4 12 N N N N 10 14
10
Output:
10
12

Explanation:
Testcase 1:
                              20
                            /    \
                          8       22
                        /   \
                      4     12
                           /   \
                         10     14
InOrder traversal gives : 4 8 10 12 14 20 22
Hence successor of 8 is 10
'''

# traverse in inorder and first value greater than given x is ans, save it and return
def inorderSuccessor(root, x):
    def findInorder(root, x, ans):
        if root == None:
            return
         
        findInorder(root.left, x, ans)
        if root.data > x.data and ans[0] == None:
            ans[0] = root
            return
        findInorder(root.right, x, ans)
        
    ans = [None]
    findInorder(root, x, ans)
    return ans[0] 
