'''
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
Expected Time Complexity: O(N)
Expected Auxialliary Space Usage: O(1)  (ie, you should not use the recursive stack space as well)
Example:
Input:
2
3
1 2 1
4
1 2 3 4
Output:
1
0
'''

def midpoint(head):
    if head == None or head.next == None:
        return head
    slow = head
    fast = head.next
    while(fast != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
    return slow
	
def reverse(head):
    if head == None or head.next == None:
        return head
    p = None
    c = head
    while(c != None):
        n = c.next
        c.next = p
        p = c
        c = n
    head = p
    return head
	
# method - 1 (iterative)
# reverse second half of ll and match first half with second half
def isPalindrome(head):
    a = head
    mid = midpoint(head)
    b = mid.next
    mid.next = None
    b = reverse(b)
    mid.next = b
    while(b!= None):
        if a.data != b.data:
            return 0
        a = a.next
        b = b.next
    return 1

# method -2 recursive -> check first and last node, and keep first node as by reference so that accesible throughout recursion and access last node acc to recursion
'''
bool check(Node **left, Node*right){
    if(right == NULL){
        return true;
    }
    
    bool isp = check(left, right->next);
    if(!isp){
        return false;
    }
    
    bool isp1 = ((*left)->data == right->data);
    if(isp1){
        (*left) = (*left)->next;
    }
    return isp1;
}
bool isPalindrome(Node *head)
{
    //Your code here
    return check(&head, head);
}	
'''