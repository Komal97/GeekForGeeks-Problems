'''
https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.
Only following standard operations are allowed on queue.
enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item
Input:
2
5 3
1 2 3 4 5
4 4
4 3 2 1
Output:
3 2 1 4 5
1 2 3 4
'''
# use circular queue, pop from front and append in stack, & inc front, and then inc rear and append values popped from stack
def reverseK(queue,k,n): # here queue = list
    stack = []
    front = 0
    rear = n-1
    for i in range(k):
        stack.append(queue[front]);
        front = (front+1)%n;
    
    for i in range(k):
        rear = (rear+1)%n
        queue[rear] = stack.pop()
    return queue