'''
https://practice.geeksforgeeks.org/problems/lucky-alive-person-in-a-circle/0
Given n people standing in a circle where 1st is having sword, find the luckiest person in the circle, 
if from 1st soldier who is having a sword each have to kill the next soldier and handover the sword to next soldier, 
in turn, the soldier will kill the adjacent soldier and handover the sword to next soldier such that one soldier remains in this war who is not killed by anyone.
Input
2
5
10
Output
3
5
'''
# keep on traversing list until one node left in circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, n):
        self.head = Node(1)
        self.head.next = self.head
        if n == 1:
            return
        tail = self.head
        for i in range(2, n+1):
            n = Node(i)
            tail.next = n
            tail = tail.next
            n.next = self.head
            
    def findAlive(self):
      
        cur = self.head
        if cur == cur.next:
            print(cur.data)
            return
            
        while(True):
            temp = cur.next
            cur.next = temp.next
            temp = None
            cur = cur.next
            if cur.next == cur:
                print(cur.data)
                return

if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        ll = CircularLinkedList()
        ll.insert(n)
        ll.findAlive()
        t -= 1
		
# method - 2 -> bitwise 
# return abs(n-complement(n))
import math
def findAlive(n):
    length = int(math.log2(n)+1)
    
    n2 = n
    for i in range(length):
        n2 ^= (1<<i)
    return abs(n-n2)