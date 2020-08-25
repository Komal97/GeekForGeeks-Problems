'''
Create graph using adjacency list.
Adjacency list is created using map and list.

Output:
Putin  ->  Trump, Modi, Pope, 
Modi  ->  Trump, Yogi, 
Trump  ->  Modi, 
Yogi  ->  Modi, Prabhu, 
Prabhu  ->  Modi, 

Explanation:
key is vertex and its value is its neighbour.
'''

from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.__h = defaultdict(list)
    
    def add_edge(self, u, v, bidirec = True):
        self.__h[u].append(v)
        if bidirec:
            self.__h[v].append(u)

    def print_list(self):

        for key in self.__h:
            print(key, ' -> ', end = ' ')
            for val in self.__h[key]:
                print(val, end = ', ')
            print()
    
g = Graph()
g.add_edge("Putin", "Trump", False)
g.add_edge("Putin", "Modi", False)
g.add_edge("Putin", "Pope", False)
g.add_edge("Modi", "Trump")
g.add_edge("Modi", "Yogi")
g.add_edge("Yogi", "Prabhu", False)
g.add_edge("Prabhu", "Modi", False)
g.print_list()
    