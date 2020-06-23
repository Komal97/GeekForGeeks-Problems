'''
https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list/0
Given a Linked List of integers, write a function to modify the linked list such that all even numbers appear before all the odd numbers 
in the modified linked list. Also, keep the order of even and odd numbers same.
Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ size of elements ≤ 1000

Example:

Input
3
7
17 15 8 9 2 4 6
4
1 3 5 7
7
8 12 10 5 4 1 6

Output
8 2 4 6 17 15 9
1 3 5 7
8 12 10 4 6 5 1
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        tail = self.head
        while(tail.link != None):
            tail = tail.link
        n = Node(data)
        tail.link = n
        n.link = None 
    
    def delete(self):
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.link
        temp = None
        
	# move all even elements in the starting
    def segregate(self):
        
        if self.head == None or self.head.link == None:
            return
        even = None
        even_tail = None
        temp = self.head
        
        while(temp != None and temp.data%2 == 0):
            if even == None:
                even = Node(temp.data)
                even_tail = even
            else:
                n = Node(temp.data)
                even_tail.link = n
                n.link = None
                even_tail = even_tail.link
            
            self.delete()
            temp = self.head
        
        if self.head != None and self.head.link != None:
            temp = self.head.link
            prev = self.head
            
            while(temp != None):
                if temp.data%2 == 0:
                    if even == None:
                        even = Node(temp.data)
                        even_tail = even
                    else:
                        n = Node(temp.data)
                        even_tail.link = n
                        n.link = None
                        even_tail = even_tail.link
                    
                    prev.link = temp.link
                    temp = None
                else:
                    prev = temp
                temp = prev.link
        if even:
            even_tail.link = self.head
            self.head = even
	
	# keep 2 pointers each for odd, even and change links of existing list and divide them into 2 list without extra memory and join them
	def segregate_2(self):
        
        if self.head == None or self.head.link == None:
            return
        even_h = None
        even_t = None
        odd_h = None
        odd_t = None
        temp = self.head
        while(temp!= None):
            if temp.data%2 == 0:
                if even_h == None:
                    even_h = temp
                    even_t = even_h
                    temp = temp.link
                else:
                    even_t.link = temp
                    temp = temp.link
                    even_t = even_t.link
                even_t.link = None
            else:
                if odd_h == None:
                    odd_h = temp
                    odd_t = odd_h
                    temp = temp.link
                else:
                    odd_t.link = temp
                    temp = temp.link
                    odd_t = odd_t.link
                odd_t.link = None
        
        if even_h:
            self.head = even_h
            if odd_h:
                even_t.link = odd_h                
        else:
            self.head = odd_h
            
    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end = " ")
            temp = temp.link
        print()
        
if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ll = LinkedList()
        for num in arr:
            ll.insert(num)
        ll.segregate_2()
        ll.printList()
        t -= 1