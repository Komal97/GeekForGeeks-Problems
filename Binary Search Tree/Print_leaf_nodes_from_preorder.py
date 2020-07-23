'''
https://practice.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst/0
Given a preorder traversal of a BST, print the leaf nodes of the tree without building the tree.
Input:
2
5
890 325 290 530 965 
3
3 2 4

Output:
290 530 965
2 4
'''

# similar to preorder to postorder
# maintain min and max, if arr finish or arr value don't lie in range, return False
# check current val has left or right, if both false means leaf 
def printLeafNodes(arr, n, min_val, max_val, pre_index):
    
    if pre_index[0] == n:
        return False
    
    if arr[pre_index[0]] < min_val or arr[pre_index[0]] > max_val:
        return False
    
    val = arr[pre_index[0]]
    pre_index[0] += 1
    
    left = printLeafNodes(arr, n, min_val, val, pre_index)
    right = printLeafNodes(arr, n, val, max_val, pre_index)
    
    if not left and not right:
        print(val, end = " ")
         
    return True
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        pre_index = [0]
        printLeafNodes(arr, n, float('-inf'), float('inf'), pre_index)
        print()
        t -= 1