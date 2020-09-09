'''
https://www.geeksforgeeks.org/xor-sum-every-possible-pair-array/
Given an array A of size n. The task is to generate a new sequence B with size N^2 having elements sum of every pair of array A and find the xor value of sum of all the pairs formed.
Note: Here (A[i], A[i]), (A[i], A[j]), (A[j], A[i]) all are considered as different pairs.
Input: arr = {1, 5, 6}
Output: 4

Explanation:
B[2*2] = { 1+1, 1+5, 1+6, 5+1, 5+5, 5+6, 6+1, 6+5, 6+6}
B[4] = { 2, 6, 7, 6, 10, 11, 7, 11, 12}
So, 2 ^ 6 ^ 7 ^ 6 ^ 10 ^ 11 ^ 7 ^ 6 ^ 11 ^ 12 = 4
'''

# write all pairs
# each pair cancel out other except pair with itself
# so ans ^= (2arr[i])
def findans(arr, n):
    
    ans = 0
    for num in arr:
        ans ^= (2*num)
    print(ans)
    
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

findans(arr, n)