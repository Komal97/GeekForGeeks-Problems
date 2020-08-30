'''
https://practice.geeksforgeeks.org/problems/bridge-edge-in-graph/1
Given an undirected graph and an edge, the task is to find if the given edge is a bridge in graph, 
i.e., removing the edge disconnects the graph.
Input:
2
4 3
0 1 1 2 2 3
1 2
5 5
1 2 2 0 1 0 3 4 3 0
2 0

Output:
1
0
'''

# remove s and e from original adjacency list and start dfs from s 
# after completing dfs, check e is visited or not, if visited means s and e is not bridge else it is bridge
from collections import defaultdict
def dfs(visited, adj, node):
    
    visited[node] = True
    for neighbor in graph[node]:
        if (not visited[neighbor]):
           dfs(visited, adj, neighbor)
    
def isBridge (adj, V, s, e):
    
    visited = defaultdict(bool)
    
    adj[s].remove(e)
    adj[e].remove(s)
    
    dfs(visited, adj, s)
    
    return not visited[e]