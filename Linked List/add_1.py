'''
A number (n) is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Input:
The First line contains the number of test cases, and for each test case a single line of input denotes an integer n.
Output:
For each test case, print the resulting number in a new line.
Input:
4
456
123
999
1879
Output:
457 
124 
1000 
1880
'''
# reverse list, add 1 then again reverse list
def addOne(head):
    #Returns new head of linked List.
    head = reverse(head)
    temp = head
    prev = None
    val = 0
    while(temp != None):
        val = temp.data + 1
        if val > 9:
            temp.data = 0
        else:
            temp.data = val
            break
        prev = temp
        temp = temp.next
  
    if val == 10:
        n = Node(1)
        prev.next = n
        n.next = None
    head = reverse(head)
    return head
