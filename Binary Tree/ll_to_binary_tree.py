'''
https://practice.geeksforgeeks.org/problems/make-binary-tree/1
Given a Linked List Representation of Complete Binary Tree. The task is to construct the Binary tree.
Input:
2
5
1 2 3 4 5
5
5 4 3 2 1
Output:
1 2 3 4 5
5 4 3 2 1

Explanation:
Testcase 1: Given tree is 
                            1
                         /     \
                       2        3
                    /      \
                  4        5
Now, the level order traversal of the above tree is 1 2 3 4 5.
'''

# method - 1
# create nodes and append in array
# then according to formula, connect nodes
def constructTree(arr):
    n = len(arr)
    root = arr[0]
    for i in range(len(arr)):
        if ((2*i) + 1) < n:
            arr[i].left = arr[2*i+1]
        if ((2*i) + 2) < n:
            arr[i].right = arr[2*i+2] 
    return root
    
def convert(head):
    
    arr = []
    temp = head
    while temp != None:
        node = BinaryTreeNode(temp.data)
        arr.append(node)
        temp = temp.next

    root = constructTree(arr)
    return root

# method - 2
# add root in queue, make it parent and push 2 next nodes from linked list, pushing is done to keep track of parent node level wise
# append 2 push nodes as left and right of parent node
from collections import deque
def convert(head):
    
    if head == None:
        return None
    
    q = deque()
    root = BinaryTreeNode(head.data)
    q.append(root)
    head = head.next
    
    while head:
        
        parent = q.popleft()
        
        leftchild = None
        rightchild = None
        
        leftchild = BinaryTreeNode(head.data)
        q.append(leftchild)
        head = head.next
        if head:
            rightchild = BinaryTreeNode(head.data)
            q.append(rightchild)
            head = head.next
        if leftchild:
            parent.left = leftchild
        if rightchild:
            parent.right = rightchild
    return root
