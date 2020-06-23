'''
https://practice.geeksforgeeks.org/problems/swap-kth-node-from-beginning-and-kth-node-from-end-in-a-singly-linked-list/1
Given a singly linked list of size N, and an integer K. You need to swap the Kth node from beginning and Kth node from the end in the linked list.
Note: You need to swap the nodes through the links and not changing the content of the nodes.
Input:
3
4 1
1 2 3 4
5 3
1 2 3 4 5
4 4
1 2 3 4
Output:
4 2 3 1
1 2 3 4 5
4 2 3 1
'''

def swapkthnode(head,num,k):
    # if k is greater than number of nodes
    if num<k:
        return head
    # if kth node from beg and end is same
    if (2*k-1) == num:
        return head
    # swap x and y pointer
	# 2 cases - x before y and y befor x
    x = head
    x_prev = Node(None)
    for i in range(k-1):
        x_prev = x
        x = x.next
    
    y = head
    y_prev = Node(None)
    for i in range(num-k):
        y_prev = y
        y = y.next
        
    if x_prev is not None:
        x_prev.next = y
    
    if y_prev is not None:
        y_prev.next = x
    
    temp = x.next
    x.next = y.next
    y.next = temp
    
    if k == 1:
        head = y
    if k == num:
        head = x
   
    return head