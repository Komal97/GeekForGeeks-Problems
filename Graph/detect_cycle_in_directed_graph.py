'''
https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Given a Directed Graph. Check whether it contains any cycle or not.
Input:
3
2 2
0 1 0 0
4 3
0 1 1 2 2 3
4 3
0 1 2 3 3 2
Output:
1
0
1

Explanation:
Testcase 1: In the above graph there are 2 vertices. The edges are as such among the vertices.
'''

# based on concept of back-edge
# to check back-edge, create an array instack 
# go depth in path and and mark instack[node]=True, if at some point instack[neighour]=True is found, means same node is is visiting again in the path 
# while returning from a path mark instack[node]=False means a path is finish 
from collections import defaultdict, deque
def checkCycle(graph, visited, node, instack):
    
    visited[node] = True
    instack[node] = True
    
    for neighbour in graph[node]:
        if not visited[neighbour] :                                         # if node not visited then check for further nodes
            if(checkCycle(graph, visited, neighbour, instack)):
                return True
        if instack[neighbour]:                                              # check if node itself form cycle 
            return True
        
    instack[node] = False
    return False
    
def isCyclic(n, graph):
    
    visited = [False]*n
    instack = [False]*n
    for i in range(n):
        if not visited[i]:
            cycle = checkCycle(graph, visited, i, instack)
            
            if cycle:
                return 1
                
    return 0