'''
https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
Input:
First line of input is the number of test cases T. Every test case has four lines. First line of every test case contains three numbers, 
x (number of nodes before merge point in 1st list), y (number of nodes before merge point in 2nd list) and z (number of nodes after merge point). 
Next three lines contain x, y and z values.
Example:
Input:
2
2 3 2
10 20
30 40 50
5 10
2 3 2
10 20
30 40 50
10 20
Output:
5
10
'''
# find length of both ll, move bigger list by diff of both lengths and then simultaneously move both pointers
def length(head):
    count = 0
    while(head != None):
        head = head.next
        count += 1
    return count
    
def intersetPoint(head_a,head_b):
    #code here
    a = length(head_a)
    b = length(head_b)
    if a > b:
        c = a-b
        while(c!=0 and head_a != None):
            head_a = head_a.next
            c -= 1
    else:
        c = b-a
        while(c!=0 and head_b != None):
            head_b = head_b.next
            c -= 1
    while(head_a != None and head_b != None):
        if head_a == head_b:
            return head_a
        head_a = head_a.next
        head_b = head_b.next
    return -1
