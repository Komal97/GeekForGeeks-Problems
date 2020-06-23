'''
Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.
Input:

2
3
1 2 3
4
1 7 3 4

Output:
1 3 2
1 4 7 3
'''
# divide list into 2 halves, reverse second half and then connect 2 list
def findMid(head):
    if head == None or head.next == None:
        return head
    fast = head.next
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow
    
def reverse(head):
    if head == None or head.next == None:
        return head
    c = head
    p = None
    while c!= None:
        n = c.next
        c.next = p
        p = c
        c = n
    head = p
    return head
    
def reorderList(self):
    if (self.head==None or self.head.next==None):
        return
    mid = findMid(self.head)
    a = self.head
    b = mid.next
    mid.next = None
    b = reverse(b)
    while(a != None and b != None):
        if a:
            temp = a
            a = a.next
        if b:
            temp.next = b
            temp = b
            b = b.next
            temp.next = a
    
        