'''
https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. 
The task is to delete the node. Pointer/ reference to head node is not given. 
Note: No head reference is given to you.
Input:
2
2
1 2
1
4
10 20 4 30
20
Output:
2
10 4 30
'''

# move next element to current position and move to next and delete last element 
def deleteNode(curr_node):
    #code here
    prev = curr_node
    while(curr_node != None and curr_node.next!=None):
        prev = curr_node
        curr_node.data = curr_node.next.data
        curr_node = curr_node.next
    prev.next = None