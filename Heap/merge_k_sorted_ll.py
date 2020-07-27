'''
https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1
Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.
Input:
2
4
3 1 2 3 2 4 5 2 5 6 2 7 8
3
2 1 3 3 4 5 6 1 8
Output:
1 2 3 4 5 5 6 7 8
1 3 4 5 6 8

Explanation :
Testcase 1: The test case has 4 sorted linked list of size 3, 2, 2, 2
1st   list     1 -> 2-> 3
2nd   list     4->5
3rd   list     5->6
4th   list     7->8
The merged list will be 1->2->3->4->5->5->6->7->8.
'''

from heapq import heappush, heappop

# build min heap
# push (node.val, node)
# set tail node, pop min node and push next node of that ll from which min belongs
# use setattr to override __lt__ (if node.data become eq then heap check for sec parameter which is node here so to compare 2 node)
def mergeKLists(arr,N): # arr contain head of each ll
    
    heap = []
    
    setattr(Node, "__lt__", lambda self, other: self.data <= other.data)    # set and override __lt__func
    
    for i in range(N):
        heappush(heap, (arr[i].data, arr[i]))
 
    root = heap[0][1]
    tail = None
    
    while len(heap) > 0:
        
        if tail == None:
            tail = heap[0][1]
        else:
            tail.next = heap[0][1]
            tail = tail.next
            
        heappop(heap)
        
        if tail and tail.next:
            heappush(heap, (tail.next.data, tail.next))
            
    return root