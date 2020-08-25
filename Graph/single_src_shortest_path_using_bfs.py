'''
https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
Given a unweighted graph, a source and a destination, we need to find shortest path from source to destination in the graph in most optimal way.
'''
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.__h = defaultdict(list)
    
    def add_edge(self, u, v, bidirec = True):
        self.__h[u].append(v)
        if bidirec:
            self.__h[v].append(u)

    def print_list(self):

        for node in self.__h:
            print(node, end = '-> ')
            for neighbour in self.__h[node]:
                print(neighbour, end = ' ')
            print()

    def bfs(self, src):

        dist = defaultdict(int)                         # distance map for src to node 
        parent = defaultdict()                          # can maintain parent also

        for node in self.__h:
            dist[node] = float('inf')                   # set distance of each node as infinity

        queue = deque()
        queue.append(src)                               # add src node and distance of src to src is 0
        dist[src] = 0

        while len(queue) > 0:
            node = queue.popleft()
            for neighbour in self.__h[node]:
                if dist[neighbour] == float('inf'):     # if distance is infinity means node is not visited 
                    dist[neighbour] = dist[node] + 1    # so update distance and add node in queue
                    queue.append(neighbour)
                    parent[neighbour] = node            # update node as parent of neighbour

        for node in dist:
            print(src, '->', node, '->', dist[node])    # print distance of each node from src node


g = Graph()
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(0,4)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(3,5)
g.add_edge(3,4)
g.print_list()
print()
g.bfs(0)