'''
https://www.geeksforgeeks.org/check-if-a-directed-graph-is-connected-or-not/
You are given a graph. You are required to find and print all connected components of the graph.
Input:
7
5
0 1 10
2 3 10
4 5 10
5 6 10
4 6 10
Output:
[[0, 1], [2, 3], [4, 5, 6]]
'''

'''
You are given a graph. You are required to find and print all connected components of the graph.
Input:
7
5
0 1 10
2 3 10
4 5 10
5 6 10
4 6 10
Output:
[[0, 1], [2, 3], [4, 5, 6]]
'''

from collections import defaultdict

class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt
        
def get_connected_components(graph, src, visited, component):
    
    visited[src] = True
    component.append(src)
    
    for edge in graph[src]:
        if not visited[edge.nbr]:
            get_connected_components(graph, edge.nbr, visited, component)


vertices = int(input())                                 
edges = int(input())  

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(edges):
    parts = list(map(int, input().split()))
    src = parts[0]
    nbr = parts[1]
    wt = parts[2]
    graph[src].append(Edge(src, nbr, wt))
    graph[nbr].append(Edge(src, nbr, wt))

ans = []
# since there is not specific source and dest, we will start from each vertex
# start from each vertex and add all its connected neighbours in an array if not visited using dfs
for i in range(vertices):                               
    component = []
    if not visited[i]:
        get_connected_components(graph, i, visited, component)
        ans.append(component)
        
# to check, graph is connected or not
if len(ans) == 1:
    print('true')
else:
    print('false')





