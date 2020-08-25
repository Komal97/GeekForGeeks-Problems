'''
https://practice.geeksforgeeks.org/problems/print-adjacency-list/0
Create graph using adjacency list.
Adjacency list is created using list of list.

Output:
0 ->  1 4 
1 ->  0 4 2 3 
2 ->  1 3 
3 ->  4 2 1 
4 ->  0 3 1 

Explanation:
key is vertex and its value is its neighbour.
'''

class Graph:
    
    def __init__(self, v):
        self.__v = v 
        self.__l = []
        for i in range(v):
            self.__l.append([])
    
    def add_edge(self, u, v, bidirec = True):
        self.__l[u].append(v)
        if bidirec:
            self.__l[v].append(u)

    def print_list(self):

        for i in range(self.__v):
            print(i, '-> ', end = ' ')
            for vertex in self.__l[i]:      # l[i] is a list at each position
                print(vertex, end = ' ')
            print()
    
g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(4,3)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
g.print_list()
    