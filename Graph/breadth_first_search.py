'''
https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
Given a directed graph. The task is to do Breadth First Search of this graph.
2
5 4
0 1 0 2 0 3 2 4
3 2
0 1 0 2

Output:
0 1 2 3 4    // BFS from node 0
0 1 2

Explanation:
Testcase 1: 
0 is connected to 1 , 2 , 3
2 is connected to 4
so starting from 0 , bfs will be 0 1 2 3 4.
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
    
    def bfs(self, src):
        
        visited = defaultdict(bool)                                 # maintain node is visited or not             
        queue = deque()                                             # maintain nodes level wise
        
        queue.append(src)                                           # add source node in queue
        visited[src] = True                                         # mark source node as visited
        
        while len(queue) > 0:
            node = queue.popleft()                                  # pop node and print
            print(node, end = ' ')
            for neighbour in self.__h[node]:                        # iterate over each neighbour of node
                if not visited[neighbour]:                          # if neighbour is not visited then mark visited and push in queue
                    visited[neighbour] = True 
                    queue.append(neighbour)

    
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
print()
