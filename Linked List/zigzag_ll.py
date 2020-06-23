'''
https://practice.geeksforgeeks.org/problems/linked-list-in-zig-zag-fashion/1
Given a Linked list, rearrange it such that converted list should be of the form a < b > c < d > e < f .. 
where a, b, c are consecutive data node of linked list and such that the order of linked list is sustained.
For example: In 11 15 20 5 10 we consider only 11 20 5 15 10 because it satisfies the above condition and 
the order of linked list. 5 20 11 15 10 is not considered as it does not follow the order of linked list.

Example:
Input:
2
4
1 2 3 4 
5
11 15 20 5 10
Output:
1 3 2 4
11 20 5 15 10

Example:
Testcase 2: In the given linked list, after arranging them as 11 < 20 > 5 < 15 > 10 in the pattern as asked above
'''
# check for alternate nodes and make current node > prev node and current node > next node
def zigzag(head_node):
    
    if head_node == None and head_node.next == None:
        return head_node
    
    prev = None
    temp = head_node
    flag = False
    while(temp != None):
        if flag:
            if prev!= None and temp.data < prev.data:
                temp.data, prev.data = prev.data, temp.data
            if temp.next != None and temp.data < temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data 
        flag = not flag
        prev = temp
        temp = temp.next
    return head_node