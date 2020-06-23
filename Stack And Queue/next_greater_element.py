'''
https://practice.geeksforgeeks.org/problems/next-larger-element/0
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their 
appearance in the array. If no such element exists, output -1 
Input
4
4
1 3 2 4
4
4 3 2 1
4
7 8 1 4
14
10 3 12 4 2 9 13 0 8 11 1 7 5 6
Output
3 4 4 -1
-1 -1 -1 -1
8 -1 4 -1
12 12 13 9 9 13 -1 8 11 -1 7 -1 6 -1
'''

# keep a stack for finding index of element. Push an element, if coming elements are less; then push them, 
# if not means we find greater element so start popping them
# due to above method, series of finding next greater element change so we maintain separate ans array
def nextLarger(arr, n):
    if n == 1:
        print(-1)
        return
    ans = [-1]*n
    stack = [0]
    for i in range(1, n):
        next = i
        if len(stack) != 0:
            top = stack.pop()
            
            while arr[top] < arr[next]:
                ans[top] = arr[next]
                if len(stack) == 0 or arr[top] > arr[next]:
                    break
                top = stack.pop()
            
            if arr[top] > arr[next]:
                stack.append(top)
        stack.append(next)
    
    print(*ans, sep = " ")
   
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        nextLarger(arr, n)
        t -= 1