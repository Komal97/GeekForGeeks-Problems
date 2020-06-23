'''
https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1
Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. 
The new list should be made with its own memory — the original lists should not be changed.
Constraints:
1 <= T <= 100
1 <= size of linked lists <= 5000
1 <= Data in linked list nodes <= 1000

Example:
Input:
2
5 4
1 2 3 4 6
2 4 6 8
4 2
10 20 40 50
15 40

Output:
2 4 6
40
'''
# keep 2 pointers for value track and if value becomes equal, add to new list
def findIntersection(head1,head2):
    
    head = None
    tail = None
    while(head1!= None and head2!=None):
        if head1.data == head2.data:
            if head == None:
                head = Node(head1.data)
                tail = head
            else:
                n = Node(head1.data)
                n.next = None
                tail.next = n
                tail = tail.next
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next
    return head