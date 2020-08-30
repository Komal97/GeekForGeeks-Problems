'''
https://practice.geeksforgeeks.org/problems/topological-sort/1
Given a Directed Graph. Find any Topological Sorting of that Graph.
Input
2
6 6
5 0 5 2 2 3 4 0 4 1 1 3
3 4
3 0 1 0 2 0

Output:
1
1

Explanation:
Testcase 1: The output 1 denotes that the order is valid.  
So, if you have implemented your function correctly, then output would be 1 for all test cases.
'''

# since due to directed graph, it is not necessary that we can reach from src to every other node - so like connected componets, we call DFS on each veretx
# we add node in stack in postorder. Postorder -> because in tree, at leaf node we get a vertex with no dependency
from collections import defaultdict
def dfs(graph, visited, node, stack):
    
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(graph, visited, neighbour, stack)
            
    stack.append(node)
    
def topoSort(n, adj):
    
    ans = []
    stack = []
    visited = defaultdict(bool)
    
    for i in range(n):
        if not visited[i]:
            dfs(adj, visited, i, stack)
    
    while len(stack)>0:
        ans.append(stack.pop())
    
    return ans