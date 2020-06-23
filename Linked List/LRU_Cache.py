'''
https://practice.geeksforgeeks.org/problems/lru-cache/1
The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
Input:
2
2
2
SET 1 2 GET 1
2
7
SET 1 2 SET 2 3 SET 1 5 SET 4 5 SET 6 7 GET 4 GET 1
Output:
2
5 -1

Explanation: 
Test Case 1: Cache Size = 2
SET 1 2 GET 1
SET 1 2 : 1 -> 2
GET 1 : Print the value corresponding to Key 1, ie 2.
'''
# to check value -> use hash O(1)
# to insert and delete -> use doubly linked list O(1)
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
        
    def __init__(self,cap):
        self.capacity = cap
        self.head = None
        self.tail = None
        self.length = 0
        self.hash = {}
        
    def use_node(self, key):
        
    #This method works in O(1)
    def get(self, key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        value = node.val
        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return value
        
    #This method works in O(1)   
    def set(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            value = node.val
            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            n = Node(key, value)
            self.hash[key] = n
            n.next = None
            if self.head == None:
                self.head = n
                self.head = self.tail
            else:
                self.tail.next = n
                n.prev = self.tail
                self.tail = n
            self.length += 1
            temp = self.head
            print(self.head, self.tail)
            if temp and (self.length > self.capacity):
                print("hi", self.length)
                self.head = temp.next
                self.head.prev = None
                del self.hash[remove.key]
                temp = None
                self.length -= 1