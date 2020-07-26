'''
https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0
Given an input stream of n integers, find the kth largest element for each element in the stream.
Input:
2
4 6
1 2 3 4 5 6
1 2
3 4

Output:
-1 -1 -1 1 2 3
3 4 

Explanation:
Testcase1:
k = 4
For 1, the 4th largest element doesn't exist so we print -1.
For 2, the 4th largest element doesn't exist so we print -1.
For 3, the 4th largest element doesn't exist so we print -1.
For 4, the 4th largest element is 1 {1, 2, 3, 4}
For 5, the 4th largest element is 2 {2, 3, 4 ,5}
for 6, the 4th largest element is 3 {3, 4, 5}
'''

from heapq import heappush, heappop

# complexity - O(nlogK)
# keep min heap of size k, push element and heapify, if size of heap > k then print top which is kth largest and pop
def KthLargest(arr, n, k):
    
    heap = []
    for i in range(n):
        heappush(heap, arr[i])
        if len(heap) < k:
            print(-1, end = ' ')
        else:
            if len(heap) > k:
                heappop(heap)
            print(heap[0], end = ' ')
            
if __name__ == '__main__':
    
    t = int(input())
    while t:
        k, n = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        KthLargest(arr, n, k)
        print()
        t -= 1
