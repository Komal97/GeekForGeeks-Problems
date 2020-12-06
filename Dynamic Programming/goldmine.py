'''
https://www.geeksforgeeks.org/gold-mine-problem/
Given a gold mine (M) of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. 
Your task is to find out maximum amount of gold which he can collect.
Input:
2
3 3 
1 3 3 2 1 4 0 6 4
2 2
1 2 3 4
Output:
12
7

TestCase 1:
[[1, 3, 3],
 [2, 1, 4],
 [0, 6, 4]]
Output : 12 
Explanation: {(1,0)->(2,1)->(2,2)}       - coordinates
'''

# recursive
def goldMine(mat, i, j, n, m):
    
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    
    right_up = goldMine(mat, i-1, j+1, n, m)
    right = goldMine(mat, i, j+1, n, m)
    right_down = goldMine(mat, i+1, j+1, n, m)
    
    return max(right, max(right_up, right_down)) + mat[i][j]

maxval = 0
for i in range(n):
    maxval = max(maxval, goldMine(mat, i, 0, n, m))    
print(maxval)
        
# smallest problem is rightmost column and biggest problem is first column so initialize last column with same value
# at each position, take max of 3 choices(right up, right and right down)
# return max from first column
def goldMine(mat, n, m):
    
    for j in range(m-2, -1, -1):
        for i in range(n):
            right_up = mat[i-1][j+1] if i > 0 else 0
            right = mat[i][j+1]
            right_down = mat[i+1][j+1] if i < n-1 else 0
            mat[i][j] += max(right, max(right_up, right_down))
            
    maxsum = 0
    for i in range(n):
        maxsum = max(maxsum, mat[i][0])
    print(maxsum)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        a = 0
        mat = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(arr[a])
                a += 1
            mat.append(row)
        goldMine(mat, n, m)    
        t -= 1