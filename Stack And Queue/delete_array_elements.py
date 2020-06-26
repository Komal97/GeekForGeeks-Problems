'''
https://practice.geeksforgeeks.org/problems/delete-array-elements-which-are-smaller-than-next-or-become-smaller/0
Given an array arr[] and a number k. The task is to delete k elements which are smaller than next element (i.e., we delete arr[i] if arr[i] < arr[i+1]) or become smaller than next because next element is deleted.
Input
4
3
3 100 1
1
5
20 10 25 30 40
2
5
23 45 11 77 18
3
2
2 5
2
Output
100 1
25 30 40
77 18
5
'''

# if current element is greater than pop elements from stack, popped elements are previous smaller elements
def delete(arr, n, k):
    
    stack = []
    for i in range(n):
        
        while k > 0 and len(stack) >0 and arr[i] > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(arr[i])
 
    print(*stack, sep = " ")
    
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        delete(arr, n, k)
        t -= 1