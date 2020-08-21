'''
https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
Given a sequence A of size N, find the length of the longest increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order. 
This subsequence is not necessarily contiguous, or unique.
Input:
2
16
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
6
5 8 3 7 9 1
Output:
6
3
Explanation:
Testcase 2: Longest increasing subsequence is of size 3 with elements (there are many subsequence, but listing one of them): 5 7 9.
'''
# at each position, store max lis to that position
# each time check for 0 to i-1 for ith element
def lis(arr, n):
    
    dp = [1]*n
    
    maxlis = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], 1+dp[j])
        
        maxlis = max(maxlis, dp[i])
    
    print(maxlis)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        lis(arr, n)
        t -= 1