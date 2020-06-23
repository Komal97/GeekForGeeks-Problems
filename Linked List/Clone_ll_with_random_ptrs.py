'''
https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
You are given a Singly Linked List with N nodes where each node next pointing to its next node. You are also given M random pointers , 
where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.
Input:
2           
4 2                                       
1 2 3 4                             
1 2 2 4
4 3
1 3 5 9
1 1 3 4
Output:
1
1
Explanation:
Testcase 1: In this test case, there are 4 nodes in linked list.  Among these 4 nodes,  2 nodes have arbit pointer set, 
rest two nodes have arbit pointer as NULL. Third line tells us the value of four nodes. The fourth line gives the information about arbitrary pointers. The first node arbit pointer is set to node 2.  The second node arbit pointer is set to node 4.
Testcase 2: In the given testcase , applying the method as stated in the abpve testcase , the output will be 1.
'''
# insert new node between 2 existing nodes and change its arbitrary value according to previous node arb value, and then detach copied list from original
def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    temp = head
    while(temp != None):
        n = Node(temp.data)
        n.next = temp.next
        temp.next = n
        temp = temp.next.next
    temp = head
    while(temp!= None):
        if temp.arb:
            temp.next.arb = temp.arb.next
        temp = temp.next.next

    copy = head.next
    temp_h = head
    temp_c = copy
    while(temp_c != None and temp_h != None):
        temp_h.next = temp_h.next.next
        temp_h = temp_h.next
        if temp_c.next:
            temp_c.next = temp_c.next.next
            temp_c = temp_c.next
    return copy 