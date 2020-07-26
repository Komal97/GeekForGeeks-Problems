'''
https://practice.geeksforgeeks.org/problems/maximum-distinct-elements-after-removing-k-elements/0
Given an array containing N elements. The task is to find maximum number of distinct elements after removing K elements from the array.
Input:
2
7 3
5 7 5 5 1 2 2
7 5
1 2 3 4 5 6 7
Output:
4
2

Explanation:
Input : A[] = {5, 7, 5, 5, 1, 2, 2}, K = 3
Output : 4
Remove 2 occurrences of element 5 and
1 occurrence of element 2.
'''

from heapq import heappush, heappop

# store freq in map
# remove elements with max freq (k * log(distinct))
# build max heap, pop freq, freq-=1, if freq!=0 push back, in end length of heap is ans
def maxDistinct(arr, n, k):
    
    h = {}
    for num in arr:
        if num not in h:
            h[num] = 1
        else:
            h[num] += 1
    heap = []
    for el in h:
        heappush(heap, (-h[el], el))
    
    while k:
        freq, el = heap[0]
        heappop(heap)
        freq = -(abs(freq) - 1)
        if freq != 0:
            heappush(heap, (freq, el))
        k -= 1
        
    print(len(heap))
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        maxDistinct(arr, n, k)
        t -= 1