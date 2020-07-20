'''
https://practice.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1
Given a BST and a key. Insert a new Node with value equal to that key into the BST. 
Input:
2
2 1 3 
4
2 1 3 N N N 6 4
1
Output:
1 2 3 4
1 2 3 4 6

Explanation:
Testcase 1: After inserting the node 4 the tree will be
                                        2
                                      /   \
                                     1     3
                                            \
                                             4
Inorder traversal will be 1 2 3 4.
Testcase 2: After inserting the node 1 the tree will be 
                                      2
                                    /   \
                                  1      3
                                /  \   /   \
                              N     N N     6
                                           /
                                          4
Inorder traversal of the above tree will be 1 2 3 4 6.
'''
# keep traversing towards left or right based on conditions
# reach last node and insert Key on left or right based on condition
def insert(root, Key):
    
    if root == None:
        root = Node(Key)
        return root
    
    temp = root
    while temp.left != None or temp.right != None:
        if temp.data > Key and temp.left:
            temp = temp.left
        elif temp.data < Key and temp.right:
            temp = temp.right
        else:
            break
    if temp.data > Key:
        temp.left = Node(Key)
    elif temp.data < Key:
        temp.right = Node(Key)
        
    return root