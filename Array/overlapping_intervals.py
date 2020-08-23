'''
https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
Given a collection of Intervals,merge all the overlapping Intervals.
For example:
Given [1,3], [2,6], [8,10], [15,18],
return [1,6], [8,10], [15,18].
Make sure the returned intervals are sorted.
Input
2
4
1 3 2 4 6 8 9 10
4
6 8 1 9 2 4 4 7
Output
1 4 6 8 9 10
1 9
'''

# sort based on start 
# use stack to keep track of previous formed interval      
def remove_overlapping(arr, n):
    
    arr = sorted(arr, key = lambda x: x[0])
    stack = []
    stack.append(arr[0])
    for i in range(1, n):
        top = stack[-1]
        if top[1] >= arr[i][0]:
            start, end = min(top[0], arr[i][0]), max(top[1], arr[i][1])
            stack.pop()
            stack.append([start, end])
        else:
            stack.append(arr[i])
    for i in range(len(stack)):
        print(*stack[i], sep = ' ', end = ' ')
        
# sort based on start
# without extra space - use same array as stack
# keep array index and put value until we find overlapping intervals, if not then increment index
def remove_overlapping(arr, n):
    
    arr = sorted(arr, key = lambda x: x[0])
    index = 0
    for i in range(1, n):
        
        if arr[index][1] >= arr[i][0]:
            start, end = min(arr[index][0], arr[i][0]), max(arr[index][1], arr[i][1])
            arr[index][0] = start
            arr[index][1] = end
        else:
            index += 1
            arr[index] = arr[i]
            
            
    for i in range(index+1):
        print(*arr[i], sep = ' ', end = ' ')
   
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        l = []
        for i in range(0, 2*n, 2):
            x, y = arr[i], arr[i+1]
            l.append([x, y])
        remove_overlapping(l, n)
        print()
        t -= 1
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        l = []
        for i in range(0, 2*n, 2):
            x, y = arr[i], arr[i+1]
            l.append([x, y])
        remove_overlapping(l, n)
        print()
        t -= 1