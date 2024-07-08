'''
https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1
Given a Cirular Linked List split it into two halves circular lists. If there are odd number of nodes in the given circular linked list 
then out of the resulting two halved lists, first list should have one node more than the second list. 
The resultant lists should also be circular lists and not linear lists.
Input:
2
3
1 5 7
4
2 6 1 5

Output:
1 5
7
2 6
1 5
'''

# find mid, make head as head1 and mid->next as head2 
class Solution:
    def splitList(self, head, head1, head2):
        slow = head
        fast = head
        
        while fast.next != head and fast.next.next != head: # to avoid reading head
            slow = slow.next
            fast = fast.next.next
        
        if fast.next.next == head: # move 1 step ahead to point to last of ll
            fast = fast.next
            
        head1 = head   
        head2 = slow.next
        slow.next = head1
        fast.next = head2
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2