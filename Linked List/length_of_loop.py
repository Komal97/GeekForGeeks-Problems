'''
Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List 
contains a loop or not and if the loop is present then return the count of nodes in a loop or else return 0.
Constraints:
1 <= T <= 100
1 <= N <= 500
0 <= C <= N-1

Example:
Input:
2
10
25 14 19 33 10 21 39 90 58 45
4
2
1 0
1
Output:
6
1
'''
# use floyd algorithm to identify loop start point, then move slow till slow = fast and count ++
def countNodesinLoop(head):
    
    slow = head
    fast = head
    
    while(fast != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    count = 0
    if slow != fast:
        return 0
    
    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    slow = slow.next
    while(slow != fast):
        slow = slow.next
        count += 1
    return count