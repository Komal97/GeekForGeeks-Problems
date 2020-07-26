/*
https://practice.geeksforgeeks.org/problems/pairs-violating-bst-property/1
You are given a Binary tree. You are required to find the number of pairs violating the BST property. In BST every element in left subtree must be less than every element in the right subtree. 
You are required to complete the function pairsViolatingBST(Node *root, int N)
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

//traverse in inorder, store in vector, use inversion count method and merge sort to find count
void inorder(Node *root, vector<int> &v){
    if(root==NULL){
        return;
    }
    inorder(root->left, v);
    v.push_back(root->data);
    inorder(root->right, v);
}
int merge(vector<int> &arr, int s, int mid, int e, int temp[]){
    
    int i = s;
    int j = mid+1;
    int k = s;
    int count = 0;
    while(i<=mid && j<=e){
        if(arr[i] < arr[j]){
            temp[k++] = arr[i++];
        }
        else{
            count += (mid-i+1);
            temp[k++] = arr[j++];
        }
    }
    
    while(i<=mid){
        temp[k++] = arr[i++];;
    }
    
    while(j<=e){
        temp[k++] = arr[j++];
    }
    
    for(int i=s; i<=e; i++){
        arr[i] = temp[i];
    }
    return count;
}

int mergeSort(vector<int> &arr, int s, int e, int temp[]){

    int count = 0;
    if(s<e){
        int mid = s+(e-s)/2;
        count += mergeSort(arr, s, mid, temp);
        count += mergeSort(arr, mid+1, e, temp);
        count += merge(arr, s, mid, e, temp);
    }
    return count%MOD;
}

int pairsViolatingBST(Node *root,int n){
    if(root==NULL){
        return 0;
    }
    vector<int> v;
    inorder(root, v);
    int temp[v.size()] = {0};
    int count = mergeSort(v, 0, v.size()-1, temp);
    
    return count;
}