'''
https://practice.geeksforgeeks.org/problems/rearrange-a-linked-list/1
Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all even positions node are together.
Assume the first element to be at position 1 followed by second element at position 2 and so on.
Constraints:
1 <= T <= 100
1 <= N <= 10000
1 <= value <= 1000

Example:
Input:
2
4
1 2 3 4
5
1 2 3 4 5

Output:
1 3 2 4
1 3 5 2 4
'''
# take ptr odd for odd positions and even ptr for even positions and start join odd positions with odd ptr and same for even position & 
#in last connect odd list with even list
def rearrangeEvenOdd(head):
    #code here
    if head == None or head.next == None or head.next.next == None:
        return head
    odd = head
    even = head.next
    head1 = even
    
    while(odd != None and even != None and odd.next != None and even.next != None):
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = head1
    return head