'''
https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication/0
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
Input:
2
5
1 2 3 4 5
3
3 3 3
Output:
38
27
'''

# k is from i to j-1
# cost is left part(i to k) + right part(k+1, j) + multiplication of new dimensions of left and right part(arr[i-1]*arr[k]*arr[j])
# return mincost 
def mcm(arr, i, j, memo):
    if i >= j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
        
    mincost = float('inf')
    for k in range(i, j):                       
        cost = mcm(arr, i, k, memo) + mcm(arr, k+1, j, memo) + (arr[i-1]*arr[k]*arr[j])
        mincost = min(cost, mincost)
        
    memo[i][j] = mincost
    return mincost
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        memo = [[-1]*(n) for _ in range(n)]
        cost = mcm(arr, 1, n-1, memo)
        print(cost)
        t -= 1