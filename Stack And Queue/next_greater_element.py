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

# since we have to find the element from right so instead of traversing from left to right, we start from right to left and keep right elements stored in stack
# if small element is encounter on top, we pop it else we print top element(represents next largest) and push current element
# if stack is empty means no element on right is greater so we print -1 
def nextLarger(arr, n):
    stack = []
    ans = []
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    print(*ans[::-1], sep = " ")

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        nextLarger(arr, n)
        t -= 1