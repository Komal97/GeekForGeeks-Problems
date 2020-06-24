'''
https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram/0
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of 
contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

Input: 
2
7
6 2 5 4 5 1 6
4
6 3 4 2
Output:
12
9

'''

def rightSmallElement(arr, n):
    stack = []
    right = []
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            right.append(n)
        else:
            right.append(stack[-1])
        stack.append(i)
    right = right[::-1]
    return right

def leftSmallElement(arr, n):
    stack = []
    left = []
    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            left.append(-1)
        else:
            left.append(stack[-1])
        stack.append(i)

    return left
    
def maxHistogramArea(arr, n):
    
    # find smaller element to left
    left = leftSmallElement(arr, n)
    
    # find smaller element to right
    right = rightSmallElement(arr, n)
    
    maxArea = -1
    for i in range(n):
        width = right[i] - left[i] - 1
        area = width * arr[i]
        maxArea = max(maxArea, area)
    return maxArea

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxHistogramArea(arr, n))
        t -= 1