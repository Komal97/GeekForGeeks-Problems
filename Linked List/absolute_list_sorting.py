'''
https://practice.geeksforgeeks.org/problems/absolute-list-sorting/1
Given a linked list L of N nodes, sorted in ascending order based on the absolute values of its data. Sort the linked list according to the actual values.
Ex: Input : 1 -> -2 -> -3 -> 4 -> -5 
    Output: -5 -> -3 -> -2 -> 1 -> 4

Constraints
1 <= T <= 100
0 <   N  <= 30
-100 <= L[i] <= 100

Input
2
3
1 -3 -4
4
0 -2 3 -10


Output
-4  -3  1
-10 -2  0  3
'''
# traverse ll, if any out of order number encounter, move it to starting
def sortList(head):
    '''
    head: head of linkedList
    
    Your method shouldn't print anything
    it should transform the passed linked list
    '''
    global ll
    if head == None or head.next == None:
        return
    temp = ll.head
    while(temp != None and temp.next != None):
        if temp.next.data < temp.data:
            ptr = temp.next
            temp.next = ptr.next
            ptr.next = ll.head
            ll.head = ptr
        else:
            temp = temp.next
