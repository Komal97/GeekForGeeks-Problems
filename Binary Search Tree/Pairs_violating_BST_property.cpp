/*
https://practice.geeksforgeeks.org/problems/pairs-violating-bst-property/1
You are given a Binary tree. You are required to find the number of pairs violating the BST property. In BST every element in left subtree must be less than every element in the right subtree. You are required to complete the function pairsViolatingBST(Node *root, int N)
Input:
2
6
50 30 L 50 60 R 30 20 L 30 25 R 60 10 L 60 40 R
2
4 5 L 4 6 R
Output:
7
1
Explanation:
The binary tree for 1st test case is-

            50
         /       \
      30          60
    /    \      /     \
  20      25   10      40
The pairs violating the BST property are: (20, 10), (25, 10), (30, 25), (30, 10), (50, 10), (50, 40), (60, 40). Hence, the result is 7.
*/

// method-1, traverse in inorder, store in vector, run nested loops and if any element > particular element is found after particular element's position then It will be counted as one pair.
#define M 1000000007
void inorder(Node *root, vector<int> &v){
    if(root==NULL){
        return;
    }
    inorder(root->left, v);
    v.push_back(root->data);
    inorder(root->right, v);
}

int pairsViolatingBST(Node *root,int n){
    if(root==NULL){
        return 0;
    }
    vector<int> v;
    inorder(root, v);
    int count = 0;
    for(int i=0; i<v.size(); i++){
        for(int j=i+1; j<v.size(); j++){
            if(v[j] < v[i]){
                count = (count+1)%M;
            }
        }
    }
    return count;
}
