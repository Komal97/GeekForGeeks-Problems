'''
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.
Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)

Example:
Input:
2
8
1 2 2 4 5 6 7 8
4
5
1 2 3 4 5
3

Output:
4 2 2 1 8 7 6 5
3 2 1 5 4
'''

# detach small ll with size of k, reverse it and attach it to new start pointer, this process continues
def rev(head):
    if head == None or head.next == None:
        return head
    c = head
    p = None
    while(c!= None):
        n = c.next
        c.next = p
        p = c
        c = n
    head = p
    return head
    
def reverse(head, k):
    
    start = None
    end = None
    while(head!= None):
        temp1 = head
        temp2 = temp1
        for i in range(1, k):
            if temp2 and temp2.next:
                temp2 = temp2.next
        head = temp2.next
        temp2.next = None
        temp1 = rev(temp1)
        if start == None:
            start = temp1
            end = start
        else:
            end.next = temp1
            end = end.next
        while(temp1.next!=None):
            temp1 = temp1.next
            end = end.next
    return start

# recursive -> reverse first k elements and call for rest
def reverse(head, k):

    c = head
    p = None
    count = 0
    n = None
    while(c is not None and count < k):
        n = c.next
        c.next = p
        p = c
        c = n
        count += 1
    if n is not None:
        head.next = reverse(n, k)
    return p