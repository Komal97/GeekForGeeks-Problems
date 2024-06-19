"""
https://www.youtube.com/watch?v=Eu1XAfmnGZ4&list=PL-Jc9J83PIiFkOETg2Ybq-FMuJjkZSGeH&index=12
You are given shell number s
You are given `r` as number of rotations, +ve for anti-clockwise and -ve for clockwise
You are required to rotate the sth shell of matrix by `r` rotations and display the matrix.

Examples:
Input : S = 2, R = 2
        mat[4][4] = {{1, 2, 3, 4},
                    {5, 6, 7, 8},
                    {9, 10, 11, 12},
                    {13, 14, 15, 16}}
Output: 1  2  3  4
        5  11  10 8
        9  7  6 12
        13 14 15 16
"""

'''
pick the elements of shell and fill in 1D array
rotate the array by `r` elements
fill back the matrix
'''


def fill_one_d_array(matrix, row, col, s):
    s_row = s - 1
    s_col = s - 1
    e_row = row - s
    e_col = col - s

    temp_arr = []

    for i in range(s_row, e_row + 1):  # left wall
        temp_arr.append(matrix[i][s_col])
    s_col += 1

    for i in range(s_col, e_col + 1):  # bottom wall
        temp_arr.append(matrix[e_row][i])
    e_row -= 1

    for i in range(e_row, s_row - 1, -1):  # right wall
        temp_arr.append(matrix[i][e_col])
    e_col -= 1

    for i in range(e_col, s_col - 1, -1):  # top wall
        temp_arr.append(matrix[s_row][i])
    s_row += 1

    return temp_arr


def rotate(temp_arr, row, col, r, s):
    s_row = s - 1
    s_col = s - 1
    e_row = row - s
    e_col = col - s

    '''
    size = (left wall + bottom wall + right wall + top wall) - 4 
         = (e_row - s_row + 1) + (e_col - s_col + 1) + (e_row + s_row + 1) + (e_col - s_col + 1) - 4
         = 2 * (e_row - s_row + 1) + 2 * (e_col - s_col + 1) - 4
         = (2 * (e_row - s_row) + 2) + (2 * (e_col - s_col) + 2) - 4
         = 2 * (e_row - s_row) + 2 * (e_col - s_col)
         = 2 * (e_row - s_row + e_col - s_col)

    '''
    size = 2 * (e_row - s_row + e_col - s_col)

    def reverse(arr, s, e):
        i = s
        j = e
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    r = r % size
    if r < 0:
        r = r + size
    reverse(temp_arr, 0, size - r - 1)
    reverse(temp_arr, size - r, size - 1)
    reverse(temp_arr, 0, size - 1)


def fill_matrix(matrix, temp_arr, row, col, s):
    s_row = s - 1
    s_col = s - 1
    e_row = row - s
    e_col = col - s

    idx = 0
    for i in range(s_row, e_row + 1):  # left wall
        matrix[i][s_col] = temp_arr[idx]
        idx += 1
    s_col += 1

    for i in range(s_col, e_col + 1):  # bottom wall
        matrix[e_row][i] = temp_arr[idx]
        idx += 1
    e_row -= 1

    for i in range(e_row, s_row - 1, -1):  # right wall
        matrix[i][e_col] = temp_arr[idx]
        idx += 1
    e_col -= 1

    for i in range(e_col, s_col - 1, -1):  # top wall
        matrix[s_row][i] = temp_arr[idx]
        idx += 1
    s_row += 1


def rotate_shell(matrix, row, col, r, s):
    print(matrix)
    temp_arr = fill_one_d_array(matrix, row, col, s)
    rotate(temp_arr, row, col, r, s)
    fill_matrix(matrix, temp_arr, row, col, s)
    print(matrix)

def main():
    row, col = 4, 4
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    r = 2  # number of rotation
    s = 2  # shell number
    rotate_shell(matrix, row, col, r, s)


main()
