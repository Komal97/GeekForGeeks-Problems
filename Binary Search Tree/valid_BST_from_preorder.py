'''
https://practice.geeksforgeeks.org/problems/preorder-traversal-and-bst/0/
Given an array arr of size n, write a program that prints 1 if given array can represent preorder traversal of a BST, else prints 0.
Input:
3
5
40 30 35 80 100
8
40 30 32 35 80 90 100 120
8
7  9 6 1 4 2 3 40

Output:
1
1
0
'''

# use min max concept, same as pre to post conversion
# check prefix index = n or not
def checkPreorder(arr, n, min_val, max_val, prefix_ind):
    
    if prefix_ind[0] == n:
        return
    
    if arr[prefix_ind[0]] < min_val or arr[prefix_ind[0]] > max_val:
        return
    
    val = arr[prefix_ind[0]]
    prefix_ind[0] += 1
    
    checkPreorder(arr, n, min_val, val, prefix_ind)
    checkPreorder(arr, n, val, max_val, prefix_ind)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        
        prefix_ind = [0]
        checkPreorder(arr, n, float('-inf'), float('inf'), prefix_ind)
        
        print(int(prefix_ind[0] == n))
        t -= 1
        