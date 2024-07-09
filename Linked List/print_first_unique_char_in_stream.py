'''
https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0
Given an input stream of N characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. 
If no non repeating element is found print -1.
Input:
2
4
a a b c
3
a a c

Output:
a -1 b b
a -1 c
'''

# always return head value
# keep track of existing node by entering in hashmap with value as node address
# if present in map, then delete node else keep adding in map
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.hash = {}
    
    def insert(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
    
    def delete(self, node):
        if node.prev == None:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev    
        else:
            self.tail = node.prev
    
    def get(self):
        if self.head:
            return self.head.data
        return -1

    def nonRepChar(self, data):
        if data not in self.hash:
            self.insert(data)
            self.hash[data] = self.tail
        else:
            if self.hash[data] != None:
                self.delete(self.hash[data])
                self.hash[data] = None
        return self.get()

    def printList(self):
        print()
        temp = self.head
        while temp:
            print(temp.data, "->", end = " ")
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        ll = DoublyLinkedList()
        string = input()
        string = [ch for ch in string if ch != ' ']
        for ch in string:
            print(ll.nonRepChar(ch), end = " ")
        print()
        t -= 1