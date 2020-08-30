'''
https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
Given a graph of V nodes represented in the form of the adjacency matrix. 
The task is to find the shortest distance of all the vertex's from the source vertex.
Input:
2
2
0 25 25 0
0
3
0 1 43 1 0 6 43 6 0
2

Output:
0 25
7 6 0
'''

from heapq import heappush, heappop
from collections import defaultdict

# shortest distance with minimum weight between 2 nodes
# same as BFS
# use minheap instead of queue to maintain nodes with min distance
# distance in heap = dist till current node + current dist
from heapq import heappush, heappop
def dijkstra(src, V, g):
    
    visited = [False]*V
    heap = []
    heappush(heap, [0, src])
    distance = [0]*V
    
    while len(heap) > 0:
        dist, node = heap[0]
        heappop(heap)
        
        if visited[node]:
            continue
        visited[node] = True
     
        distance[node] = dist
        
        for i in range(V):
            if visited[i] == False and g[node][i] != 0:
                heappush(heap, [g[node][i]+dist, i])
    return distance