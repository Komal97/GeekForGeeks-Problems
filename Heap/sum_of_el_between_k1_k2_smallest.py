'''
https://practice.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements/0
Given an array of positive integers and two positive integers K1 and K2. Find sum of all elements greater tha K1th and smaller than K2th smallest elements of array.
Input
2
7
20 8 22 4 12 10 14
3 6
6
10 2 50 12 48 13
2 6

Output:
26
73

Explanation:
Test Case 1:
3rd smallest element is 10
6th smallest element is 20
Sum of all element between K1 & K2 is 12 + 14 = 26
'''
from heapq import heapify, heappush, heapreplace

# find k1th smallest el and k2th smallest element
# sum of all element lie between k1 and k2th smallest element
def findKthSmallest(arr, n, k):
    
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
        k1, k2 = list(map(int, input().split()))
        
        first = findKthSmallest(arr, n, k1)
        second = findKthSmallest(arr, n, k2)
        summ = 0
        
        for i in range(n):
            if arr[i] > first and arr[i] < second:
                summ += arr[i]
        print(summ)
        t -= 1