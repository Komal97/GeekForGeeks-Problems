'''
https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. 
If all the nodes in the linked list are equal, then remove n-1 nodes.
Example:
Input:
2
4
5 2 2 4
5
2 2 2 2 2
Output:
5 2 4
2
'''
def removeDuplicates(head):
   
    if head == None or head.next == None:
        return head
    
    prev = None
    temp = head
    s = set()

    while(temp != None):
        if temp.data in s:
            prev.next = temp.next
            temp = None
        else:
            s.add(temp.data)
            prev = temp
        temp = prev.next
    return head
