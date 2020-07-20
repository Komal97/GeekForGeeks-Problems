/*
https://practice.geeksforgeeks.org/problems/construct-bst-from-post-order/1
Given postorder traversal of a Binary Search Tree, you need to complete the function constructTree() which will create a BST. The output will be the inorder of the constructed BST.
Input:
2
6
1 7 5 50 40 10
9
216 823 476 429 850 93 18 975 862

Output:
1 5 7 10 40 50
18 93 216 429 476 823 850 862 975
Explanation:
Testcase 1: The BST for the given post order traversal is:
        10
      /    \ 
     5      40
   /  \       \
  1    7       50
*/

Node *constructTree (int post[], int size)
{   
    if(size==0){
        return NULL;
    }
    else if(size==1){
        Node *root = new Node(post[0]);
        return root;
    }

    stack<Node *> s;
    Node *root = new Node(post[size-1]);
    s.push(root);
   
    for(int i=size-2; i>=0; i--){
        
        Node *node = new Node(post[i]);

        // if current node is greater than stack top, then connect current node to top right and push current for later reference so that it can also become root
        if(post[i] > s.top()->data){
            s.top()->right = node;
            s.push(node);
        }
        // if current data is less than stack top means if is on left of some node, so keep popping until it get element less than itself
        // and connect current data on left of last popped node and push current for later reference so that it can also become root
        else{
            Node *temp = NULL;
            while(s.size()>0 && s.top()->data > post[i]){
                temp = s.top();
                s.pop();
            }
            temp->left = node;
            s.push(node);
        }
    }
    return root;
}