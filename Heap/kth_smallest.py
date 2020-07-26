'''
https://practice.geeksforgeeks.org/problems/kth-smallest-element/0 
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
Output:
7
15
'''

from heapq import heapify, heappush, heapreplace

# complexity - O(nlogK)
# keep max heap of size k, if size of heap > k then pop max and push and heapify
# push -ve of element because by default heap is minheap
def kthsmallest(arr, n, k):
    
    heap = []
    heapify(heap)
    
    for i in range(n):
        if len(heap) < k:
            heappush(heap, -arr[i])
        elif heap[0] < -arr[i]:
            heapreplace(heap, -arr[i])
    return -heap[0]

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        print(kthsmallest(arr, n, k))
        t -= 1
        