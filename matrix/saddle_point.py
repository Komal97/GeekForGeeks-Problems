'''
https://www.geeksforgeeks.org/saddle-point-matrix/
Given a matrix of n x n size, the task is to find the saddle point of the matrix. 
A saddle point is an element of the matrix such that it is the minimum element in its row and the maximum in its column. 

Examples : 
Input: Mat[3][3] = { {1, 2, 3},
                  {4, 5, 6},
                  {7, 8, 9}}
Output: 7
7 is minimum in its row and maximum in its column.

Input: Mat[3][3] = {{1, 2, 3},
                    {4, 5, 6},
                    {10, 18, 4}}
Output: No saddle point
'''

# matrix can have one saddle point

def findSaddlePoint(row, col, arr):
    for i in range(row): #traverse each row
        # for each row, find column with min value
        minJ = 0
        for j in range(col):
            if arr[i][j] < arr[i][minJ]:
                minJ = j

        # check if current value is max in all the rows of minJ col
        flag = True
        for k in range(row): 
            if arr[k][minJ] > arr[i][minJ]: # if other value is greater
                flag = False                # means current [i][minJ] is not saddlePoint
                break
        
        if flag:      # if saddlePoint found then return
            print(arr[i][minJ])
            return

    print("invalid")

row, col = list(map(int, input().split()))
arr = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    arr.append(a)

findSaddlePoint(row, col, arr)