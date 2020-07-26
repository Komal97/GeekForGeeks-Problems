'''
https://practice.geeksforgeeks.org/problems/k-largest-elements/0
Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed in decreasing order.
Input:
2
5 2
12 5 787 1 23
7 3
1 23 12 9 30 2 50

Output:
787 23
50 30 23
'''

# complexity - O(nlogK)
# keep min heap of size k, if size of heap > k then pop min and push and heapify
# works in data stream also
from heapq import heapify, heappush, heapreplace, nlargest
def klargest(arr, n, k):
    
    heap = []
    heapify(heap)
    
    for i in range(n):
        # if size of heap < k, add elements in heap
        if len(heap) < k:
            heappush(heap, arr[i])
        # else remove min element and then push new element
        elif heap[0] < arr[i]:
            heapreplace(heap, arr[i])
    
    print(*nlargest(k, heap), sep = ' ')

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        klargest(arr, n, k)
        t -= 1