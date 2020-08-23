'''
https://practice.geeksforgeeks.org/problems/length-unsorted-subarray/0
Given an unsorted array A of size N. Find the subarray A[s..e] such that sorting this subarray makes the whole array sorted.
Input:
2
11
10 12 20 30 25 40 32 31 35 50 60
9
0 1 15 25 6 7 30 40 50

Output:
3 8
2 5

Explanation:
Testcase 1: Subarray starting from index 3 and ending at index 8 is required subarray.
Initial array: 10 12 20 30 25 40 32 31 35 50 60
Final array:  10 12 20 25 30 31 32 35 40 50 60  (After sorting the bold part)
'''

# method - 1 => maintain stack of indexes
def nextlarger(arr, n):
    
    # keep indexes in stack of continous increasing element from 0 to n else pop
    stack = []
    stack.append(0)
    for i in range(1, n):
        while len(stack) > 0 and arr[i] < arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    
    # now check first out of order index in stack
    ind = 0
    for i in range(len(stack)):
        if ind != stack[i]:
            return ind
        ind += 1
    
    return 0 if ind == n else ind+1

def leftSmaller(arr, n):
    
    # keep indexes in stack of continous decreasing element from n to 0 else pop 
    stack = []
    stack.append(n-1)
    for i in range(n-2, -1, -1):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    
    # now check first out of order index in stack
    ind = n-1
    for i in range(len(stack)):
        if ind != stack[i]:
            return ind
        ind -= 1
    
    return 0 if ind == 0 else ind-1
    
def length_unsorted(arr, n):
    start = 0
    end = 0
    if n == 1:
        print(start, end)
        return
    elif n == 2:
        if arr[0] > arr[1]:
            end = 1
        print(start, end)
        return
    start = nextlarger(arr, n)
    end = leftSmaller(arr, n)
    print(start, end)

# method - 2
def length_unsorted(arr, n):
    
    s = 0
    e = 0
    
    # step-1 => find candidate array (out of order indexes)
    # find s=i if arr[i] > arr[i+1] from left to right
    # find e=i if arr[i-1] > arr[i] from right to left  
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            s = i
            break
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            e = i
            break
       
    # between this array is always unsorted, and to expand it find min and max val between this array    
    min_val = float('inf')
    max_val = float('-inf')
    for i in range(s, e+1):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])
    
    # step-2 => elements on left should by smaller and on right, it should be greater
    # find first greater value than minval from 0 to s-1
    start = s
    for i in range(s):
        if arr[i] > min_val:
            start = i
            break
        
    # find first smaller value than maxval from n to e+1
    end = e
    for i in range(n-1, e, -1):
        if arr[i] < max_val:
            end = i
            break
    print(start, end)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        length_unsorted(arr, n)
        t -= 1
