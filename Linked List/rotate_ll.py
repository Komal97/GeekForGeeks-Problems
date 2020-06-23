'''
https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1
Given a singly linked list of size N. 
The task is to rotate the linked list counter-clockwise by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= k <= 103

Example:
Input:
2
8
1 2 3 4 5 6 7 8
4
5
2 4 7 8 9
3
Output:
5 6 7 8 1 2 3 4
8 9 2 4 7
Explanation:
Testcase 1: After rotating the linked list by 4 elements (anti-clockwise), we reached to node 5, which is (k+1)th node from beginning, 
now becomes head and tail of the linked list is joined to the previous head.
Testcase 2: After rotating the linked list by 3 elements (anti-clockwise), we will get the resulting linked list as 8 9 2 4 7.
'''
# keep 2 pointers, one -> head, second is at k+1 node, move first half to second half
def rotateList(head, k):
    # code here
    if head == None or head.next == None:
        return head
    a = head
    while(k>1):
        a = a.next
        k -= 1
    b = a.next
    if b:
        a.next = None
        head_b = b
        while(b != None and b.next != None):
            b = b.next
        
        b.next = head
        return head_b
    return head