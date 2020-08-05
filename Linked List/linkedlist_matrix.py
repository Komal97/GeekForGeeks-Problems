'''
https://practice.geeksforgeeks.org/problems/linked-list-matrix/1
Given a Matrix mat of N*N size, the task is to complete the function constructLinkedMatrix(), that constructs a 2D linked list representation of the given matrix.
Input : 2D matrix 
1 2 3
4 5 6
7 8 9

Output :
1 -> 2 -> 3 -> NULL
|    |    |
v    v    v
4 -> 5 -> 6 -> NULL
|    |    |
v    v    v
7 -> 8 -> 9 -> NULL
|    |    |
v    v    v
NULL NULL NULL
Input:
2
3
1 2 3 4 5 6 7 8 9
2
1 2 3 4
Output:
1 2 3 4 5 6 7 8 9
1 2 3 4
'''
# method - 1 (Recursive)
# recursively call on down and right pointer of a node
def build(arr, i, j, n):
    if i == n or j == n:
        return None
    
    node = Node(arr[i][j])
    node.right = build(arr, i, j+1, n)
    node.down = build(arr, i+1, j, n)
    return node
    
def construct(arr, n):
    return build(arr, 0, 0, n)
    
# method - 2 (Iterative)
# in first iteration -> create separate linkedlist of each row by maintaining head of each ll in an array
# in second iteration -> join down of head[i] with head[i+1] 
def construct(arr, n):
    
    mainhead = None
    head = [None]*(n+1)             # create array of head of each row
    for i in range(n):
        temp = None
        for j in range(n):
            node = Node(arr[i][j])
            if not mainhead:        # set arr[0][0] as mainhead
                mainhead = node
            if not head[i]:         # set head of each ll
                head[i] = node
                temp = head[i]
            else:
                temp.right = node   # otherwise move to right of that ll
            temp = node   

    for i in range(n):
        temp1 = head[i]             # take 2 ll and join their right pointer
        temp2 = head[i+1]
        
        while temp1 and temp2:  
            temp1.down = temp2
            temp1 = temp1.right
            temp2 = temp2.right
            
    return mainhead
        