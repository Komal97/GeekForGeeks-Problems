'''
https://practice.geeksforgeeks.org/problems/smallest-number-on-left/0iption/
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.
If no small element present on the left print -1.

Input:
2
3
1 6 2
6
1 5 0 3 4 5

Output:
-1 1 1
-1 1 -1 0 3 4
'''

# same as largest element to left
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    stack = []
    ans = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    print(*ans, sep = ' ')
    t -= 1
