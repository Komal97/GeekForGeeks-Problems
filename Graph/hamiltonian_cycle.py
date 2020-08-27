'''
https://practice.geeksforgeeks.org/problems/hamiltonian-path/0
A Hamiltonian path, is a path in an undirected or directed graph that visits each vertex exactly once. 
Given an undirected graph  the task is to check if a Hamiltonian path is present in it or not.
Input:
2
4 4
1 2 2 3 3 4 2 4
4 3
1 2 2 3 2 4
Output:
1
0
'''

from collections import defaultdict

# keep count, if count == number of vertex, means we found a path
# since src is not mentioned so take each vertex as starting point
def is_path_hamiltonian(graph, visited, src, count, v):
    if count == v:
        return True
        
    visited[src] = True
    for neighbour in graph[src]:
        if not visited[neighbour]:
            path_found = is_path_hamiltonian(graph, visited, neighbour, count+1, v)
            if path_found:
                return True
    visited[src] = False
    
    return False
    
t = int(input())
while t:
    v, e = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    visited = defaultdict(bool)
    for i in range(0, 2*e, 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])

    for i in range(1, v+1):
        if not visited[i]:
            ans = is_path_hamiltonian(graph, visited, i, 1, v)
            if ans :
                break
    print(int(ans))
    t -= 1

