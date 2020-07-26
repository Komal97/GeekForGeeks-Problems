'''
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0
There are given N ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.
Input:
2
4
4 3 2 6
5
4 2 7 6 9

Output:
29
62
'''

from heapq import heapify, heappush, heappop

# build minheap
# each time, we need 2 min elements to make cost min
# after adding 2 min elements in cost, add them in heap again
def minCostOfRopes(arr, n):
    
    heapify(arr)
    cost = 0
    while len(arr) > 0:
        first = arr[0]
        heappop(arr)
        second = arr[0]
        heappop(arr)
        
        cost += (first + second)
        
        heappush(arr, first + second)
        if len(arr) == 1:
            break
    
    print(cost)
if __name__ == '__main__':
   
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        minCostOfRopes(arr, n)
        t -= 1