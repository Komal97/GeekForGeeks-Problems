/*
https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1
Given a Cirular Linked List split it into two halves circular lists. If there are odd number of nodes in the given circular linked list 
then out of the resulting two halved lists, first list should have one node more than the second list. 
The resultant lists should also be circular lists and not linear lists.
Input:
2
3
1 5 7
4
2 6 1 5

Output:
1 5
7
2 6
1 5
*/

// find mid, make head as head1 and mid->next as head2 
void splitList(Node *head, Node **head1_ref, Node **head2_ref)
{
    // your code goes here
    Node *fast = head;
    Node *slow = head;
   
    while(fast->next!=head && fast->next->next!=head){
        fast = fast->next->next;
        slow = slow ->next;
    }
    if(fast->next->next==head){
        fast = fast->next;
    }
    (*head1_ref) = head;
    (*head2_ref) = slow->next;
    fast->next = slow->next;
    slow->next = (*head1_ref);
    
}