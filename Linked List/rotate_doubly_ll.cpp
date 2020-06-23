/*
Given a doubly linked list, rotate the linked list counter-clockwise by P nodes. 
Here P is a given positive integer and is smaller than the count of nodes(N) in a linked list.Input:
1
6 2
1 2 3 4 5 6

Output:
3 4 5 6 1 2
*/

// keep 2 pointers, 1 at first and 2 is head in second half, then move first half to second half
struct node*update(struct node*start,int p)
{
    //Add your code here
    node *temp1 = start;
    for(int i=0; i<p; i++){
        start = start->next;
    }
    start->prev->next = NULL;
    start->prev = NULL;
    node *temp2 = start;
    while(temp2 !=NULL && temp2->next != NULL){
        temp2 = temp2->next;
    }
    temp2->next = temp1;
    temp1->prev = temp2;
    
    return start;
}