'''
https://practice.geeksforgeeks.org/problems/row-with-max-1s/0
Given a boolean 2D array where each row is sorted. Find the row with the maximum number of 1s.
Input:
2
4 4
0 1 1 1 0 0 1 1 1 1 1 1 0 0 0 0
2 2
0 0 1 1

Output:
2
1

Explanation :
Testcase 1 : Row 2 is having maximum number of 1s (0-based indexing).
'''

# start from first row and top right corner
# since each row is sorted so, row with min col number has maximum 1s
def read_matrix(matrix, r, c):
    data = map(int, input().split())
    matrix = [*map(list, zip(*[data] * c))]
    return matrix

def row_with_max_1(matrix, r, c):
    i = 0
    j = c-1
    pos = 0
    while(i<r and j>=0):
        if matrix[i][j-1]==1:           # if 1 encounter then col-1 and save current row
            pos = i
            j -= 1
        else:                           # if 0 encounter then row+1
            i += 1
    return pos
    
def main():
    t = int(input())
    while(t):
        r, c = list(map(int, input().split()))
        matrix = []
        matrix = read_matrix(matrix, r, c)
        print(row_with_max_1(matrix, r, c))
        t -= 1
main()