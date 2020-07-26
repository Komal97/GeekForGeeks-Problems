'''
https://practice.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1
Given K sorted lists of integers of size N each, find the smallest range that includes at least one element from each of the K lists. If more than one such range's are found, print the first such range found.
Input:
2
5 3
1 3 5 7 9
0 2 4 6 8
2 3 5 7 11
4 3
1 2 3 4
5 6 7 8
9 10 11 12

Output:
1 2
4 9

Explanation:
Testcase1: K = 3
A:[1 3 5 7 9]
B:[0 2 4 6 8]
C:[2 3 5 7 11]
Smallest range is formed by number 1 present in first list and 2 is present in both 2nd and 3rd list.
'''

# same as merge k sorted array
# use min heap, keep track of max element, and min difference(maxel - top)
from heapq import heappush, heappop
def smallestRange(numbers):

    heap = []
    diff = float('inf')
    maxel = float('-inf')
    
    for i in range(len(numbers)):
        maxel = max(maxel, numbers[i][0])
        heappush(heap, [numbers[i][0], [i, 0]])
    
    ans = []
    while True:
        
        i = heap[0][1][0]
        j = heap[0][1][1] + 1
        minel = heap[0][0]
        heappop(heap)
        
        if maxel-minel < diff:
            diff = maxel-minel
            ans = [minel, maxel]
        
        if j < len(numbers[0]):
            maxel = max(maxel, numbers[i][j])
            heappush(heap, [numbers[i][j], [i, j]])
        else:
            break
    print(*ans, sep = ' ')