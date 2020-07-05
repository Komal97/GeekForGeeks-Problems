'''
https://practice.geeksforgeeks.org/problems/merge-sort-on-doubly-linked-list/1
Given Pointer/Reference to the head of a doubly linked list of N nodes, the task is to Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing order.
Input:
2
8
7 3 5 2 6 4 1 8
5
9 15 0 -1 0
Output:
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
-1 0 0 9 15
15 9 0 0 -1
'''

def merge(a, b):
    if a == None:
        return b
    if b == None:
        return a
        
    if a.data <= b.data:
        head = a
        a = a.next
    else:
        head = b
        b = b.next
        
    temp = head
    while a!= None and b!= None:
        if a.data <= b.data:
            temp.next = a
            a = a.next
        else:
            temp.next = b
            b = b.next
        temp.next.prev = temp
        temp = temp.next
    if a:
        temp.next = a
        a.prev = temp
    if b:
        temp.next = b
        b.prev = temp
    return head
    
def findmid(head):
    if head == None or head.next == None:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def sortDoubly(head):
    if head == None or head.next == None:
        return head
        
    mid = findmid(head)
    a = head
    b = mid.next
    b.prev = None
    mid.next = None
    a = sortDoubly(a)
    b = sortDoubly(b)
    c = merge(a, b)
    return c