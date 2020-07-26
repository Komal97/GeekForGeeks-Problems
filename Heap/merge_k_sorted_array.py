'''
https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
Input:
2
3
1 2 3 4 5 6 7 8 9 
4
1 2 3 4 2 2 3 4 5 5 6 6 7 8 9 9

Output:
1 2 3 4 5 6 7 8 9
1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 

Explanation:
Testcase 1:
Above test case has 3 sorted arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''

from heapq import heappush, heappop, heapreplace

# build min heap of size k (complexity - nlogk)
def merge(numbers):
    
    k = len(numbers)
    n = len(numbers[0])
    heap = []
    
    # push first element of each array (num, (i, j))
    ans = []
    for i in range(k):
        heappush(heap, [numbers[i][0], [i, 0]])
    
    # keep poping min element and push next element of that array from which min belongs
    while len(heap)>0:
        top = heap[0]
        ans.append(top[0])
        heappop(heap)
        i = top[1][0]
        j = top[1][1]+1
        if j<k:
            heappush(heap, [numbers[i][j], [i, j]])
    
    return ans