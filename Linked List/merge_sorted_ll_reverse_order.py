'''
Given two linked lists of size N and M, which are sorted in non-decreasing order. 
The task is to merge them in such a way that the resulting list is in decreasing order.
Constraints:
1 <=T<= 50
1 <= N, M <= 1000

Example:
Input:
2
4 3
5 10 15 40 
2 3 20
2 2
1 1
2 4

Output:
40 20 15 10 5 3 2
4 2 1 1 
'''
# method - 1 -> reverse both list and merge
def reverse(head):
    if head == None or head.next == None:
        return head
    
    c = head
    p = None
    while(c!=None):
        n = c.next
        c.next = p
        p = c
        c = n
    head = p
    return head

def merge(h1, h2):
    if h1 == None:
        return h2
    elif h2 == None:
        return h1
    
    if h1.data < h2.data:
        c = h2
        c.next = merge(h1,h2.next)
    else:
        c = h1
        c.next = merge(h1.next,h2)
        
    return c
    
def mergeResult(h1,h2):
    #return head of merged list
    h1 = reverse(h1)
    h2 = reverse(h2)
    return merge(h1, h2)
	

# method - 2 - > create resultant list with small element between h1 and h2 append in beginning
def add(head, data):
    n = Node(data)
    n.next = head
    head = n
    return head
def mergeResult(h1,h2):
    #return head of merged list
    
    res = None
    while(h1 != None and h2 != None):
        if h1.data<=h2.data:
            data = h1.data
            h1 = h1.next
        else:
            data = h2.data
            h2 = h2.next
        res = add(res, data)
    
    while(h1):
        res = add(res, h1.data)
        h1 = h1.next
    while(h2):
        res = add(res, h2.data)
        h2 = h2.next
    return res