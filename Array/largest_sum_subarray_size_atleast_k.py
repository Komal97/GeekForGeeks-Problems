'''
https://practice.geeksforgeeks.org/problems/largest-sum-subarray-of-size-at-least-k/0
Given an array and a number k, find the largest sum of the subarray containing at least k numbers. It may be assumed that the size of array is at-least k.
Input:
2
4
-4 -2 1 -3
2
6
1 1 1 1 1 1
2

Output:
-1
6
'''

# use kadane's
def largest_sum_subarray(arr, n, k):

    # calculate total sum of initial k size window
    total = 0
    for i in range(k):
        total += arr[i]
    
    prev = arr[0]
    maxsum = total          # value of first window
    csum = total
    j = 1
    for i in range(k, n):
        total += arr[i]
        csum += arr[i]
        # total-prev = k means include current elemnt in k size window or prev big window
        csum = max(csum, (total-prev))      
        prev += arr[j]
        j += 1
        maxsum = max(maxsum, csum)
    print(maxsum)

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    largest_sum_subarray(arr, n, k)
    t -= 1