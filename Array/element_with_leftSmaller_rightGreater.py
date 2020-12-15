'''
https://practice.geeksforgeeks.org/problems/unsorted-array/0
Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.
Input:
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9

Output:
5
-1
7
'''

# method - 1
# create left max array and right min storing max/min value before/after current position
# at current position, check (arr[i] >= left_max) and (arr[i] <= right_min)
def getElement(arr, n):
    
    right_min = [float('inf')]*n
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], arr[i+1])

    left_max = float('-inf')
    for i in range(1, n-1):
        left_max = max(left_max, arr[i-1])
        if (arr[i] >= left_max) and (arr[i] <= right_min[i]):
            return arr[i]
        
    return -1

# method - 2
def getElement(arr, n):
    
    if n <= 2:
        return -1
    
    max_val = arr[0]            # left maximum value
    element = arr[0]            # potential value
    idx = -1                    # index of potential value
    bit = -1                    # check whether element is from if condition or else
    #check = 0
    
    i = 1
    while i < (n-1):
        
        # if current element is less so it is not potential value
        if arr[i] < max_val and i < (n-1):
            i += 1
            bit = 0
        else:
            
            # it is potential value
            if arr[i] >= max_val:
                element = arr[i]
                idx = i
                max_val = arr[i]
                #check = 1
            
            #if check == 1:
            i += 1
            
            # update bit state that we found potential value
            bit = 1 
            
            # process all elements after current element as they are greater
            while i < (n-1) and arr[i] >= element:
                if arr[i] > max_val:
                    max_val = arr[i]
                i += 1
            #check = 0
            
    # it checks element is not from extreme ends and element is not updated after else condition
    if element <= arr[n-1] and bit == 1:
        return arr[idx]
    else:
        return -1
    
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = getElement(arr, n)
    print(ans)
    t -= 1