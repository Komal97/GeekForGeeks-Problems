'''
https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.
Input:
4
5
15
1 
3
Output:
5
10
5
4
 
Explanation:
Testcase 1:
Flow in stream : 5, 15, 1, 3
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)
'''

from heapq import heappush, heappop

if __name__ == '__main__':
    n = int(input())
    
    lheap = []           # max heap
    rheap = []           # min heap
    
    # use 2 heaps , max(left) & min(right)
    # max will store elements less than median and min will store elements greater than median
    while n:
        num = int(input())
        
        # push in left if both are empty or num < left.top else push in second
        if len(lheap) == 0 and len(rheap) == 0:
            heappush(lheap, -num)
        elif num < -lheap[0]:
            heappush(lheap, -num)
        else:
            heappush(rheap, num)
        
        # if imbalance, pop from imbalanced heap and push in balanced
        if abs(len(lheap) - len(rheap)) > 1:
            if len(lheap) > len(rheap):
                heappush(rheap, -lheap[0])
                heappop(lheap)
            else:
                heappush(lheap, -rheap[0])
                heappop(rheap)
        
        # if even length then avg else top of heap whose length is greater
        if len(lheap) == len(rheap):
            print(((-lheap[0]) + rheap[0])//2)
        elif len(lheap) > len(rheap):
            print(-lheap[0])
        else:
            print(rheap[0])
        
        n -= 1
        
        