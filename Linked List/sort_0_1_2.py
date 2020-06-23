'''
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. 
The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side,
2s at the end of the linked list, and 1s in the mid of 0s and 2s.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
8
1 2 2 1 2 0 2 2
4
2 2 0 1
Output:
0 1 1 2 2 2 2 2
0 1 2 2
'''
# keep count of 0, 1, 2 and fill list from start
def segregate(head):
    #code here
    count0 = 0
    count1 = 0
    count2 = 0
    temp = head
    while(temp != None):
        if temp.data == 0:
            count0 += 1
        elif temp.data == 1:
            count1 += 1
        elif temp.data == 2:
            count2 += 1
        temp = temp.next
    
    temp = head
    while(count0 > 0 and temp != None):
        temp.data = 0
        temp = temp.next
        count0 -= 1 
    
    while(count1 > 0 and temp != None):
        temp.data = 1
        temp = temp.next
        count1 -= 1
    
    while(count2 > 0 and temp != None):
        temp.data = 2
        temp = temp.next
        count2 -= 1
    return head
	
# keep 3 pointers each for 0,1,2 and change links of existing list and divide them into 3 list without extra memory and join them 
def segregate(head):
    zero_h = None
    zero_t = None
    one_h = None
    one_t = None
    two_h = None
    two_t = None
    temp = head
    while(temp!= None):
        if temp.data == 0:
            if zero_h == None:
                zero_h = temp
                temp = temp.next
                zero_t = zero_h
            else:
                zero_t.next = temp
                temp = temp.next
                zero_t = zero_t.next
            zero_t.next = None
        elif temp.data == 1:
            if one_h == None:
                one_h = temp
                temp = temp.next
                one_t = one_h
            else:
                one_t.next = temp
                temp = temp.next
                one_t = one_t.next
            one_t.next = None
        elif temp.data == 2:
            if two_h == None:
                two_h = temp
                temp = temp.next
                two_t = two_h
            else:
                two_t.next = temp
                temp = temp.next
                two_t = two_t.next
            two_t.next = None
    if zero_t and one_h:
        zero_t.next = one_h
    elif zero_t and two_h:
        zero_t.next = two_h
    if one_t and two_h:
        one_t.next = two_h
    if zero_h:
        head = zero_h
    elif one_h:
        head = one_h
    elif two_h:
        head = two_h
    return head