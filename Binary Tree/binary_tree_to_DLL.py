'''
https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
Input:
2
1 3 2
10 20 30 40 60
Output:
3 1 2
2 1 3
40 20 60 10 30
30 10 60 20 40

Explanation:
Testcase2: The tree is
                           10
                         /    \
                       20     30
                     /    \
                   40      60
So, DLL would be 40<=>20<=>60<=>10<=>30.
'''

# method - 1 => maintain head and tail pointer of LL (same as binary tree to singly ll)
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

def convertBTtoDLL(root):
    
    pair = DLL()
    if root == None:
        return pair
    
    lpair = convertBTtoDLL(root.left)
    rpair = convertBTtoDLL(root.right)
    
    if root.left == None and root.right == None:
        pair.head = root
        pair.tail = root
    
    elif root.left and root.right == None:
        root.left = lpair.tail
        lpair.tail.right = root
        pair.head = lpair.head
        pair.tail = root
    
    elif root.right and root.left == None:
        root.right = rpair.head
        rpair.head.left = root
        pair.head = root
        pair.tail = rpair.tail
    
    else:
        root.left = lpair.tail
        lpair.tail.right = root
        root.right = rpair.head
        rpair.head.left = root
        pair.head = lpair.head
        pair.tail = rpair.tail
    return pair
    
def bToDLL(root):
    
    if root == None or (root.left == None and root.right == None):
        return root
        
    return convertBTtoDLL(root).head

# method - 2 => maintain prev node while inorder traversal
# if prev = None, means we reach first leaf node, then assign it to head, after that change left and right pointers of prev and root
def convertBTtoDLL(root, head, prev):
    
    if root == None:
        return
    
    convertBTtoDLL(root.left, head, prev)
    
    if prev[0] == None:
        head[0] = root
    else:
        root.left = prev[0]
        prev[0].right = root
    prev[0] = root
    convertBTtoDLL(root.right, head, prev)
    
def bToDLL(root):
    
    if root == None or (root.left == None and root.right == None):
        return root
        
    head = [None]
    prev = [None]
    convertBTtoDLL(root, head, prev)

    return head[0]
