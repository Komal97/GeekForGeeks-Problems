'''
https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
Implememt depth first search traversal on graph.
'''
from collections import deque, defaultdict
class Graph:
    
    def __init__(self):
        self.__h = defaultdict(list)                                # create blank dictionary of list
    
    def add_edge(self, u, v, bidirec = True):
        self.__h[u].append(v)
        if bidirec:
            self.__h[v].append(u)

    def print_list(self):

        for key in self.__h:                                        # consider each node
            print(key, ' -> ', end = ' ')
            for val in self.__h[key]:                               # print neighbours of key node
                print(val, end = ', ')
            print()

    # recursion goes in depth so we use recursion for dfs
    def dfs_helper(self,node, visited):
        
        visited[node] = True                                        # mark node as visited and print
        print(node, end = ' ')

        for neighbour in self.__h[node]:                            # recursively call on neighbours if they are not visited
            if not visited[neighbour]:
                self.dfs_helper(neighbour, visited)

    def dfs(self):
        visited = defaultdict(bool)
        self.dfs_helper(0, visited)                                 # pass source node and visited array
        print()
    
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
g.dfs()
