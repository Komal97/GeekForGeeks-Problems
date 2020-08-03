'''
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
Input
1
8
15 -2 2 -8 1 7 10 23

Output
5
'''

# use prefix sum technique
# keep map {sum: index}, initally h = {0, -1}
# keep adding number in sum, if that has encountered earlier means elements between 2 equal sum make sum=0
def maxLen(n, arr):
    
    h = {0 : -1}
    maxlen = 0
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ in h:
            maxlen = max(maxlen, i-h[summ])
        else:
            h[summ] = i

    return maxlen