'''
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
Given a Linked List of size N, where every node represents a linked list and contains two pointers of its type:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
You have to flatten the linked list to a single linked list which should be sorted.

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
And after flattening the above list, the sorted linked list looks like:
5-> 7-> 8- > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50.
'''
# merge 2 adjacent ll and do this using recursion
def merge(a, b):
    if a == None:
        return b
    if b == None:
        return a
    
    if a.data<b.data:
        c = a
        c.bottom = merge(a.bottom, b)
    else:
        c = b
        c.bottom = merge(a, b.bottom)
    return c
    
def flatten(root):
    #Your code here
    if root == None or root.next == None:
        return root
    
    merged_head = flatten(root.next)
    return merge(root, merged_head)