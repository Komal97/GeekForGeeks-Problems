'''
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/nearest-smaller-element-929558b4/description/
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
SAMPLE INPUT 
8
39 27 11 4 24 32 32 1
SAMPLE OUTPUT 
-1 -1 -1 -1 4 24 24 -1
'''

# same as largest element to left
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