'''
https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. 
The sum list is a linked list representation of the addition of two input numbers.
Note:
The linked list has been constructed in the reverse order of the number. That is if the number is given is 123 then the linked list representing 
it is 3 -> 2 -> 1.
Hence, the resultant number to be printed will be in reverse order(rightmost digit as head and followed by digits to its left)
Example:
Input:
2
2
4 5
3
3 4 5
2
6 3
1
7
Output:
0 9 3 
0 7
'''
# list are already reversed, so add them 
def length(head):
    count = 0
    while(head!=None):
        head = head.next
        count += 1
    return count
    
def addBoth(l1,l2):
    if not l1:
        return l2
    elif not l2:
        return l1 
    
    temp = l1 if length(l1)>length(l2) else l2
    head = temp
    carry = 0
    while(l1 != None or l2 !=None):
        num = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry
        temp.data = num%10
        carry = num//10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        prev = temp
        temp = temp.next

    if carry:
        x = Node(carry)
        prev.next = x
        x.next = None
    return head