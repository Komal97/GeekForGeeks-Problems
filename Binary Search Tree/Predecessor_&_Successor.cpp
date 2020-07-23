/*
https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1
There is BST given with root node with key part as integer only. You need to find the inorder successor and predecessor of a given key. In case, if the either of predecessor or successor is not found print -1.
Input:
2
6
50 30 L 30 20 L 30 40 R 50 70 R 70 60 L 70 80 R
65
6
50 30 L 30 20 L 30 40 R 50 70 R 70 60 L 70 80 R
100

Output:
60 70
80 -1
*/

// assign value to predecessor until root->data < key 
// assign value to successor if it is null and just greater than given key and return
void findPreSuc(Node* root, Node*& pre, Node*& suc, int key)
{
    if(root==NULL){
        return;
    }
    
    findPreSuc(root->left, pre, suc, key);
    if(root->key < key){
        pre = root;
    }
    else if(suc == NULL && root->key > key){
        suc = root;
        return;
    }
    findPreSuc(root->right, pre, suc, key);

}