'''
https://practice.geeksforgeeks.org/problems/print-all-nodes-that-dont-have-sibling/1
Given a Binary Tree of size N, such that all nodes have distinct values, print all the nodes which don't have a sibling node in sorted order. If all nodes have a sibling node then print -1 .

Example:
Input
2
37 20 N 113 
1 2 3
Output 
20 113
-1
Explanation:
Testcase 1: In above example the root node is 37 which has left child 20 and right child nothing. The node 20 has a left child 113. 
So, the aswer is 2 that is node 20 and 113 don't have siblings.
'''

# send current node as parent and its left and right node
# if any parent has one child, then print that one child
def printSibling(root):
    
    def printSingle(node, parent, ans):
        if node == None:
            return
        
        if parent != None and parent.left != None and parent.right == None:
            ans.append(node.data)
        elif parent != None and parent.right != None and parent.left == None:
            ans.append(node.data)

        printSingle(node.left, node, ans)
        printSingle(node.right, node, ans)
    ans = []
    printSingle(root, None, ans)
    if len(ans) == 0:
        print(-1, end = '')
    else:
        ans = sorted(ans)
        print(*ans, sep = ' ', end = '')