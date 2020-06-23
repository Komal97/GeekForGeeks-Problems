/*
Theory link - https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/
https://practice.geeksforgeeks.org/problems/xor-linked-list/1
Given stream of data of size N for the linked list, your task is to complete the function insert() and printList(). 
The insert() function pushes (or inserts at beginning) the given data in the linked list and the printList() 
function prints the linked list first in forward direction and then in backward direction.
Note: There is an utility function XOR() that takes two Node pointer to get the bit-wise XOR of the two Node pointer. 
Use this function to get the XOR of the two pointers.
Input:
2
6
9 5 4 7 3 10
3
58 96 31

Output:
10 3 7 4 5 9
9 5 4 7 3 10
31 96 58
58 96 31
*/


/*struct Node* XOR (struct Node *a, struct Node *b)
{
	return (struct Node*) ((uintptr_t) (a) ^ (uintptr_t) (b));
}*/

// function should insert the data to the front of the list
void insert(struct Node **head_ref, int data)
{
	Node *n = new Node(data);
	n->npx = (*head_ref);
	
	if((*head_ref)!=NULL){
	    (*head_ref)->npx = XOR(n, (*head_ref)->npx);
	}
    (*head_ref) = n;
}

// function should prints the contents of doubly linked list
// first in forward direction and then in backward direction
// you should print a next line after printing in forward direction
void printList (struct Node *head)
{
	Node *prev = NULL;
	Node *curr = head;
	Node *next;
	
	while(curr!=NULL){
	    cout<<curr->data<<" ";
	    next = XOR(prev, curr->npx);
	    prev = curr;
	    curr = next;
	}
	cout<<endl;
	while(prev != NULL){
	    cout<<prev->data<<" ";
	    next = XOR(curr, prev->npx);
	    curr = prev;
	    prev = next;
	}
}