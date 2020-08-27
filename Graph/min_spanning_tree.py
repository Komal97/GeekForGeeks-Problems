'''
https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
Given a weighted, undirected and connected graph. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
Input:
2
3 3
1 2 5 2 3 3 1 3 1
2 1
1 2 5

Output:
4
5

Example:
Testcase 1:  Sum of weights of edges in the minimum spanning tree is 4.
'''

# Same as dijkstra, just save current weight in minheap instead of total
from heapq import heappush, heappop
def spanningTree(V, E, graph):
    
    summ = 0
    heap = []
    heappush(heap, [0, 0])
    visited = [False]*V
    
    while len(heap) > 0:
        dist, node = heap[0]
        heappop(heap)
        
        if visited[node]:
            continue
        
        summ += dist
        
        visited[node] = True
        
        for i in range(V):
            if visited[i] == False and graph[node][i] != float('inf'):
                heappush(heap, [graph[node][i], i])

    return summ