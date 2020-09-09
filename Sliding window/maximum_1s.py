'''
https://practice.geeksforgeeks.org/problems/maximize-number-of-1s/0
Given a binary array A of size N and an integer M. Find the maximum number of consecutive 1's produced by flipping at most M 0's.
Input:
1
11
1 0 0 1 1 0 1 0 1 1 1
2

Output:
8

Explanation:
Testcase 1: Maximum subarray is of size 8 which can be made subarray of all 1 after flipping two zeros to 1.
'''

# keep a count of zero, if count > m then reduce window size
def max_1(arr, n, m):
    
    i = 0
    j = 0
    
    max_count = 0
    zero_count = 0
    while j < n:
        if arr[j] == 0:
            zero_count += 1
            max_count = max(max_count, j-i)
            while zero_count > m and i < n:
                if arr[i] == 0:
                    zero_count -= 1
                i += 1
        j += 1
    max_count = max(max_count, j-i)
    print(max_count)    
    
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    max_1(arr, n, m)
    t -= 1