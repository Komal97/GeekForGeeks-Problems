'''
Given an array A of size N having distinct elements, the task is to find the next greater element to left 
for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input
2
4
1 3 2 4
4
4 3 2 1

Output
-1 -1 3 -1
-1 4 3 2
'''

def nextLargerToRight(arr, n):
    stack = []
    ans = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    print(*ans, sep = " ")
    

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        nextLargerToRight(arr, n)
        t -= 1