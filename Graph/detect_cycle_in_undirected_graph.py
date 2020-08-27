'''
Given a Undirected Graph. Check whether it contains a cycle or not. 
Input:
3
2 1
0 1
4 3
0 1 1 2 2 3
5 4
0 1 2 3 3 4 4 2

Output:
0
0
1

Explanation:
Testcase 1: There is a graph with 2 vertices and 1 edge from 0 to 1. So there is no cycle.
Testcase 2: There is a graph with 3 vertices and 3 edges from 0 to 1, 1 to 2 and 2 to 3.
Testcase 3: There is a cycle in the given graph formed by vertices 2, 3 and 4.
'''

# start from each vertex as there can be more than 1 component
# BFS => mark visited while popping bacause same node pushed from 2 different paths and can be identified easily
# while removing, if node is already visited, means this node is visited by 2 paths so cycle is there
from collections import defaultdict, deque
def has_cycle(g, src, visited):
    
    queue = deque() 
    queue.append(src)                                # append src
    
    while len(queue) > 0:
        node = queue.popleft()                       # remove node
        if visited[node]:
            return True
        visited[node] = True                         # mark visited
        for neighbour in g[node]:                    # append all neighbours
            if not visited[neighbour]:
                queue.append(neighbour)
                
    return False
    
def isCyclic(g,n):

    visited = defaultdict(bool)
    
    for i in range(n):                               # start from each vertex as there can be more than 1 component
        if not visited[i]:
            cycle = has_cycle(g, i, visited)
            if cycle:
                return 1
    return 0