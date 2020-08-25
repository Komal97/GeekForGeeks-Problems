'''
https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0
Given a snake and ladder board of order 5x6, find the minimum number of dice throws required to reach the destination or last cell (30th cell) from source (1st cell) . 
There are 2*N space separated values a,b which denotes a ladder or a snake at position 'a' which takes to a position 'b'.
Input:
2
6
11 26 3 22 5 8 20 29 27 1 21 9
1
2 30

Output:
3
1

Explanation:
Testcase 1:
For 1st throw get a 2, which contains ladder to reach 22
For 2nd throw get a 6, which will lead to 28
Finally get a 2, to reach at the end 30. Thus 3 dice throws required to reach 30.
'''

# since to find = min moves means find shortest path from src to dest which can be acheived using bfs
from collections import defaultdict, deque
def shortest_path_bfs(graph, src, dest):
    
    queue = deque()
    parent = defaultdict()
    dist = defaultdict(int)
    
    for node in range(31):
        dist[node] = float('inf')
    
    queue.append(src)
    dist[src] = 0
    
    while len(queue) > 0:
        node = queue.popleft()
        for neighbour in graph[node]:
            if dist[neighbour] == float('inf'):
                queue.append(neighbour)
                dist[neighbour] = dist[node] + 1
                parent[neighbour] = node
    
    # temp = dest                                     # print path from dest to src because we have parent stored
    # while temp != src:
    #     print(temp, end = ' <- ')
    #     temp = parent[temp]
    # print(src)
        
    return dist[dest]

# create a board of snake and ladder
# if +ve means ladder => board[2] = 13 means from 2 reach 2+13 = 15 so edge will created is 1 -> 15 instead of 1 -> 2
# if -ve means snake => board[17] = -13 means from 17 reach 17-13 = 4
def min_moves(arr, n):
    
    board = [0]*31
    for i in range(0, 2*n, 2):
        board[arr[i]] = arr[i+1] - arr[i]

    graph = defaultdict(list)                       # create graph as adjacency list using map of list
    
    for u in range(31):                             # create edges from each point to all 6 possibilities
        for dice in range(1, 7):
            if u+dice <= 30:
                v = u + dice + board[u + dice]
                graph[u].append(v)
            
    ans = shortest_path_bfs(graph, 1, 30)
    print(ans)
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        min_moves(arr, n)
        t -= 1
        
        
        