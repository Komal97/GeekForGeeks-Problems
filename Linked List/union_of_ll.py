'''
https://practice.geeksforgeeks.org/problems/union-of-two-linked-list/1
Given two linked lists, your task is to complete the function makeUnion(), that returns the union of two linked lists. 
This union should include all the distinct elements only.
Expected Auxilliary Space : O(1)

Example:
Input:
1
6
9 6 4 2 3 8
5
1 2 8 6 2

Output:
1 2 3 4 6 8 9
'''
# join 2 list, sort them using merge sort and then delete continuous duplicates
from sys import setrecursionlimit
setrecursionlimit(10000)
def merge(a, b):
    if a == None:
        return b
    if b == None:
        return a
    
    if a.data<=b.data:
        c = a
        c.next = merge(a.next, b)
    else:
        c = b
        c.next = merge(a, b.next)
    return c

def midpoint(head):
    if head == None or head.next == None:
        return head
    fast = head.next
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow
    
def mergesort(head):
    if head == None or head.next == None:
        return head
    
    mid = midpoint(head)
    a = head
    b = mid.next
    mid.next = None
    a = mergesort(a)
    b = mergesort(b)
    c = merge(a, b)
    return c
    
def union(head1,head2):
    temp = head1
    while temp.next != None:
        temp = temp.next
    temp.next = head2
    head1 = mergesort(head1)
    temp = head1
    while(temp):
        if temp.next and temp.data == temp.next.data:
            ptr = temp.next
            temp.next = ptr.next
            ptr = None
        else:
            temp = temp.next
    return head1
	
# using hashmap
def union(head1,head2):
    h = {}
    while head1!=None:
        h[head1.data] = head1
        head1 = head1.next
    while head2!=None:
        h[head2.data] = head2
        head2 = head2.next
    
    h = sorted(h.items(), key = lambda x: x[0])
    head = None
    tail = None
    for key, val in h:
        if head == None:
            head = Node(key)
            tail = head
        else:
            n = Node(key)
            n.next = None
            tail.next = n
            tail = n
    return head