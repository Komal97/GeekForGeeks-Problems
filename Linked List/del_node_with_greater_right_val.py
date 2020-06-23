'''
https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1
Given a singly linked list, remove all the nodes which have a greater value on its next adjacent element.
Input:
3
8
12 15 10 11 5 6 2 3
6
10 20 30 40 50 60
6
60 50 40 30 20 10

Output:
15 11 6 3
60
60 50 40 30 20 10

Explanation:
Testcase 1: Since, 12, 10, 5 and 2 are the elements which have greater elements on their next node. 
So, after deleting them, the linked list would like be 15, 11, 6, 3.
'''
# reverse list, maintain mex and delete values less than max and again reverse
# idea is to delete all elements before current element which is small
def reverse(head):
    if head == None or head.next == None:
        return head
    
    c = head
    p = None
    while c!=None:
        n = c.next
        c.next = p
        p = c
        c = n
    head = p
    return head
def compute(head):
    head = reverse(head)
    prev = Node(None)
    temp = head
    max_val = temp.data
    while(temp!=None):
        if temp.data >= max_val:
            prev = temp
            max_val = temp.data
            temp = temp.next
        else:
            prev.next = temp.next
            temp = None
            temp = prev.next
            
    head = reverse(head)
    return head
	
# use recursion -> take right pointer to last and check right and head at that point of recursion
from sys import setrecursionlimit
setrecursionlimit(2000)
def compute(head):
    
    if head == None or head.next == None:
        return head
    
    right = compute(head.next)
    if head.data < right.data:
        head = None
        return right
    else:
        head.next = right
    return head