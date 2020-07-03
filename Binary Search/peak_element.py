'''
https://practice.geeksforgeeks.org/problems/peak-element/1
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index (0 based indexing).
Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.
Input:
2
3
1 2 3
2
3 4
Output:
1
1

Explanation:
Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.
Testcase 2: 4 is the peak element as it is greater than its neighbour elements.
'''

# check for middle, if it fulfills cond then return else move to that part where probability of having peak element is maximum
# if element of mid+1 > mid then move to right part else left part
def peakElement(arr, n):
    
    if n == 1:
        return 0
    
    s = 0
    e = n-1
    while s<=e:
        mid = s + (e-s)//2 
        if mid > 0 and mid < n-1:
            if arr[mid]>=arr[mid-1] and arr[mid] >= arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                s = mid+1
            else:
                e = mid-1
        elif mid == 0:
            if arr[0]>arr[1]:
                return 0
            else:
                return 1
        elif mid == n-1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2