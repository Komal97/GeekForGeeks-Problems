'''
https://practice.geeksforgeeks.org/problems/row-with-minimum-number-of-1s/0
Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise. 
If two or more rows have same number of 1's than print the row with smallest index.
Input:
2
3 3
0 0 0 0 0 0 0 0 0
4 4
0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1

Output:
-1
0

Explanation:
Testcase 2: The matrix formed for the given input will be as such
0 0 0 1
0 1 1 1
0 0 1 1
0 0 1 1
First row is having minimum number of 1 i.e. answer is 0.
'''

# start from first row and first column
# since each row is sorted then row with min 1 has max column number
def rowWithMin1(mat, n, m):
    
    i = 0
    j = 0
    row = -1
    col = -1
    while i < n and j < m:  
        if mat[i][m-1] == 0:            # ignore row with all zeroes
            i += 1
        elif mat[i][j] == 0:            # if current element is 0 then col++
            j += 1
        else:                           # if current element is 1 then row++
            if col != j:                # check 1 in prev row and if not in same column(keep track) 
                row = i                 # save that row
                col = j
            i += 1
            
    return row
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        
        a = 0
        mat = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[a]
                a += 1
                
        print(rowWithMin1(mat, n, m))
        t -= 1