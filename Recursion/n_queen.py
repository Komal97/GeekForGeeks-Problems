'''
https://practice.geeksforgeeks.org/problems/n-queen-problem/0
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. 
Given an integer n, print all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, 
where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number.
Input
2
1
4
Output:
[1 ]
[2 4 1 3 ] [3 1 4 2 ]
'''
def isQueenSafe(mat, row, col, n):
    
    # check vertical in prv rows
    for i in range(row-1, -1, -1):
        if mat[i][col] == 1:
            return False
    
    # check left diagonal in prv rows
    i = row-1
    j = col-1
    while i >=0 and j >= 0:
        if mat[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # check right diagonal in prv rows
    i = row-1
    j = col+1
    while i >=0 and j < n:
        if mat[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    return True

# what we are doing -> consider place queen in a row and column and try to place queens in coming up rows
# if we reach last row then print and always return if we reach at wrong config or last row
# after returning, we try to place queen in different column if current row and repeat above steps again
def nQueen(mat, n, row, ans, flag):
    
    # if queens are placed successfully in all rows
    if row == n:
        print('[' + ans + ']', end = ' ')
        flag[0] = 1                                                 # maintained to check if there is any possibility or not
        return
    
    for col in range(n):                                            # for curr row, check which column is safe to place
        if isQueenSafe(mat, row, col, n):                           # check current place is safe to place queen
            mat[row][col] = 1                                       # place queen
            nQueen(mat, n, row+1, ans + str(col+1) + ' ', flag)     # proceed for further rows and save current column
            mat[row][col] = 0                                       # while returning remove queen from its place so that current place can be use in next possibility
    
if __name__ == '__main__':
    t = int(input())
    while t:
        flag = [0]
        n = int(input())
        mat = [[0 for _ in range(n)] for _ in range(n)]
        nQueen(mat, n, 0, '', flag)
        print(-1) if flag[0] == 0 else print()
        t -= 1