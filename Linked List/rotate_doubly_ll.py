'''
https://practice.geeksforgeeks.org/problems/rotate-doubly-linked-list-by-p-nodes/1
Given a doubly linked list, rotate the linked list counter-clockwise by P nodes. 
Here P is a given positive integer and is smaller than the count of nodes(N) in a linked list.Input:
1
6 2
1 2 3 4 5 6

Output:
3 4 5 6 1 2
'''

class Solution:
    def update(self, start, p):
        temp1 = start
        for i in range(p):
            start = start.next
        
        start.prev.next = None
        start.prev = None
        
        temp2 = start
        while temp2 and temp2.next:
            temp2 = temp2.next
        
        temp2.next = temp1
        temp1.prev = temp2

        return start
    