'''
https://www.geeksforgeeks.org/next-smaller-element/#:~:text=Elements%20for%20which%20no%20smaller,next%20smaller%20element%20as%20%2D1.
Given an array, print the Next Smaller Element (NSE) for every element. The Smaller smaller Element for an element x is the first smaller element on the right side of x in array. Elements for which no smaller element exist (on right side), consider next smaller element as -1.
Input:
2
5
4 2 1 5 3
6
5 6 2 3 1 7
Output:
2 1 -1 3 -1
2 2 1 1 -1 -1
'''

# same as largest element to right
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    stack = []
    ans = []
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    print(*ans[::-1], sep = ' ')
    t -= 1