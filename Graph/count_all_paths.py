'''
https://practice.geeksforgeeks.org/problems/count-the-paths/0
Given a directed graph, a source vertex ‘s’ and a destination vertex ‘d’, print the count of all paths from given ‘s’ to ‘d’.
First line of every test case consists of V and E, denoting the vertices and edges. Second line of every test case consists of 2*E spaced integers denoting the edge between vertices. 
Third line of every test case consists of S and D.
Input:
1
4 6
0 1 0 2 0 3 2 0 2 1 1 3
2 3
Output:
3
'''

def dfs(src, dest, graph, visited):
    if src == dest:
        return 1
    
    count = 0
    visited[src] = True
    for neighbour in graph[src]:
        if not visited[neighbour]:
            count += dfs(neighbour, dest, graph, visited)
            
    visited[src] = False
    return count
    
def count_paths(v, e, arr, src, dest):
    
    graph = defaultdict(list)
    visited = defaultdict(bool)
    for i in range(0, 2*e, 2):
        graph[arr[i]].append(arr[i+1])
    
    count = dfs(src, dest, graph, visited)
    print(count)

if __name__ == '__main__':
    t = int(input())
    while t:
        v, e = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        src, dest = list(map(int, input().split()))
        count_paths(v, e, arr, src, dest)
        t -= 1