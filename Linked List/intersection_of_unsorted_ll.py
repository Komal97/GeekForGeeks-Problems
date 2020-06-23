'''
https://practice.geeksforgeeks.org/problems/intersection-of-two-linked-list/1
Given two linked lists, the task is to complete the function findIntersection(), that returns the intersection of two linked lists. 
Each of the two linked list contains distinct node values.
Example:
Input:
1
6
9 6 4 2 3 8
4
1 2 8 6
Output:
6 2 8
'''

# save first ll in hashmap and traverse second and check if element present in hash
def findIntersection(head1, head2):
  
    h = {}
    head = None
    tail = None
    while(head2 != None):
        h[head2.data] = head2
        head2 = head2.next
    while(head1 != None):
        if head1.data in h:
            if head == None:
                head = Node(head1.data)
                tail = head
            else:
                n = Node(head1.data)
                n.next = None
                tail.next = n
                tail = tail.next
        head1 = head1.next
    return head