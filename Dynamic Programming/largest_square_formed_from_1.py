'''
https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix/0
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
Input:
3
5 6
0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 1
2 2
1 1 1 1
2 2
0 0 0 0

Output:
3
2
0
'''

def largest_square(mat, r, c):
    
    dp = [[0]*(c+1) for _ in range(r+1)]
    
    max_count = float('-inf')
    for i in range(1, r+1):
        for j in range(1, c+1):
            # means it can contribute to square, so take smallest square from all 3 sides and add current
            if mat[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1]) + 1      
            # means it won't contribute means no sqaure can start or end   
            else:
                dp[i][j] = 0
            # maximum square side can be found anywhere in grid
            max_count = max(max_count, dp[i][j])        
                
    print(max_count)
    
t = int(input())
while t:
    r, c = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    mat = []
    k = 0
    for i in range(r):
        row = []
        for j in range(c):
            row.append(arr[k])
            k += 1
        mat.append(row)
    
    largest_square(mat, r, c)
    
    t -= 1