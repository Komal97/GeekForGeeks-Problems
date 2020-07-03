'''
https://practice.geeksforgeeks.org/problems/boolean-matrix-problem/0
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1.
Input:
3
2 2
1 0
0 0
2 3
0 0 0 
0 0 1
4 3
1 0 0
1 0 0
1 0 0
0 0 0

Output:
1 1
1 0
0 0 1
1 1 1
1 1 1
1 1 1
1 1 1
1 0 0
'''
# with extra space, keep row and col array, if mat[i][j] == 1 set corresponding row as 1 and col as 1 and traverse again and change matrix
def boolean_matrix(matrix, r, c):
    row = [0]*r
    col = [0]*c
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                row[i] = 1
                col[j] = 1
                
    for i in range(r):
        for j in range(c):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 1
                
    for i in range(r):
        print(*matrix[i], sep = " ")
    
# without extra space, behave first col and first row as auxilliary arrays and store matrix[0][0] value in separate flag
def boolean_matrix(matrix, r, c):
    
    flag = False
    if matrix[0][0] == 1:
        flag = True
        
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                matrix[i][0] = 1
                matrix[0][j] = 1
                
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 1 or matrix[0][j] == 1:
                matrix[i][j] = 1
    
    if flag == True:
        for i in range(r):
            matrix[i][0] = 1
        for i in range(c):
            matrix[0][i] = 1
        
    for i in range(r):
        print(*matrix[i], sep = " ")
        
if __name__ == '__main__':
    t = int(input())
    while t:
        r, c = list(map(int, input().split()))
        matrix = []
        for i in range(r):
            row = list(map(int, input().split()))
            matrix.append(row)
        boolean_matrix(matrix, r, c)
        t -= 1