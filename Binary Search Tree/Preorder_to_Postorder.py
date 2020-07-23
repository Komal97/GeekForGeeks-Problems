'''
https://practice.geeksforgeeks.org/problems/preorder-to-postorder/0
Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its postorder traversal.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N) [Function call stack size].
Input:
3
5
40 30 35 80 100
8
40 30 32 35 80 90 100 120

Output:
35 30 100 80 40
35 32 30 120 100 90 80 40
'''

# maintain min and max value concept
# if array finish or element don't lie in range return
# else check element is in which range (left or right)
# indirectly behaving array like a tree and traverse that in postorder
def pre_to_post(arr, n, min_val, max_val, pre_index):
    
    if pre_index[0] == n:
        return
    
    if arr[pre_index[0]] < min_val or arr[pre_index[0]] > max_val:
        return
    
    val = arr[pre_index[0]]
    pre_index[0] += 1
    
    pre_to_post(arr, n, min_val, val, pre_index)
    pre_to_post(arr, n, val, max_val, pre_index)
    print(val, end = " ")

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        pre_index = [0]
        pre_to_post(arr, n, float('-inf'), float('inf'), pre_index)
        print()
        t -= 1