'''
https://practice.geeksforgeeks.org/problems/search-in-a-matrix/0
Given a matrix mat[] of size n x m, where every row and column is sorted in increasing order, and a number x is given. The task is to find whether element x is present in the matrix or not.
Expected Time Complexity : O(m + n)
Input:
2
3 3
3 30 38 44 52 54 57 60 69
62
1 6
18 21 27 38 55 67
55

Output:
0
1

Explanation:
Testcase 1: 62 is not present in the matrix, so output is 0.
Testcase 2: 55 is present in the matrix at 5th cell.
'''

# start from top right corner, if element > key, col-- else row++ because if current element is greater then element below it in same column are also greater 
# so we check for previous columns and if current element is small that means element may be present in same column below it

import numpy as np
def readMatrix(matrix, r, c):
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(r, c)
    return matrix
    
def search(matrix, r, c, key):
    
    i = 0
    j = c-1
    while i < r and j >= 0:
        if matrix[i][j] == key:
            return 1
        elif matrix[i][j] < key:
            i += 1
        else:
            j -= 1
    return 0
    
def main():
    t = int(input())
    while(t):
        r, c = input().split()
        r, c = int(r), int(c)
        matrix = []
        matrix = readMatrix(matrix, r, c)
        key = int(input())
        print(search(matrix, r, c, key))
        t -= 1
    
main()