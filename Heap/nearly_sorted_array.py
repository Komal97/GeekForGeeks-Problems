'''
https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
Given an array of n elements, where each element is at most k away from its target position. The task is to print array in sorted form.
Input:
2
3 3
2 1 3
6 3
2 6 3 12 56 8
Output:
1 2 3
2 3 6 8 12 56
'''
from heapq import heapify, heappush, heappop

# same as kth smallest number
# use min heap of size k, if len(heap) > k, print min element and pop 
def kSorted(arr, n, k):
    
    heap = []
    heapify(heap)
    
    for num in arr:
        if len(heap) > k:
            print(heap[0], end = ' ')
            heappop(heap)
        heappush(heap, num)
    
    while len(heap) > 0:
        print(heap[0], end = ' ')
        heappop(heap)
    
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        kSorted(arr, n, k)
        print()
        t -= 1