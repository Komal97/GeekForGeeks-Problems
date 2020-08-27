'''
https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach.
Input:
2
5 4
0 1 0 2 0 3 2 4
4 3
0 1 1 2 0 3

Output:
0 1 2 4 3   
0 1 2 3

Explanation:
Testcase 1:
0 is connected to 1 , 2 , 3
1 is connected to 0
2 is connected to 0 and 4
3 is connected to 0
4 is connected to 2
so starting from 0 , dfs will be 0 1 2 4 3.
'''

from collections import deque, defaultdict

# iterative DFS - like iterative BFS - use stack instead of queue
def dfs(g,N):
    
    ans = []
    visited = defaultdict(bool)
    stack = [0]
    
    while len(stack) > 0:
        
        node = stack.pop()
        
        if visited[node] :
            continue
        
        ans.append(node)
        visited[node] = True
        for i in range(len(g[node])-1, -1, -1):
            if not visited[g[node][i]]:
                stack.append(g[node][i])
    return ans

# recursive DFS
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

