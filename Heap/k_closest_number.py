'''
https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/
Given an unsorted array and two numbers x and k, find k closest values to x.
Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 
Output : 4 6 7
Three closest values of x are 4, 6 and 7.

Input : arr[] = {-10, -50, 20, 17, 80}, x = 20, k = 2
Output : 17, 20
'''

from heapq import heapify, heappush, heapreplace, heappop

# elements are closest if there diff is minimum so each time need min diff
# so build max heap with pair (diff, element), find k elements with 3 minimum difference
def kClosest(arr, n, k, x):
    
    heap = []
    heapify(heap)
    
    for i in range(n):
        if len(heap)<k:
            pair = (-abs(arr[i]-x), arr[i])
            heappush(heap, pair)
        elif heap[0][1] < -abs(arr[i]-x):
            pair = (-abs(arr[i]-x), arr[i])
            heapreplace(heap, pair)
                
    while len(heap) > 0:
        print(heap[0][1], end = ' ')
        heappop(heap)
    

n = int(input())
arr = list(map(int, input().split()))
k, x = list(map(int, input().split()))
kClosest(arr, n, k, x)
       