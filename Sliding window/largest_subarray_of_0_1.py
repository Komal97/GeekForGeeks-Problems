'''
https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1
Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.
Input
2
4
0 1 0 1
5
0 0 1 0 0

Output
4
2
'''
# keep count, if 0 count-- else count++ =, if anytime count becomes equal to value which is previosly encountered means 
# till now number of 0 and 1 becomes equal
def maxLen(arr, N):
    maxlen = 0
    count = 0
    h = {0 : -1}
    for i in range(N):
        if arr[i] == 1:
            count += 1
        else:
            count -= 1
        if count in h:
            maxlen = max(maxlen, i-h[count])
        else:
            h[count] = i
    return maxlen