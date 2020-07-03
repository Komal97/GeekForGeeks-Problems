'''
https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Examples:
A[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

A[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}
'''

# use 2 pointers i&j, increment j until sum becomes greater than or equal k, and after that find out min length
# start incrementing i until Sum becomes less k again
def smallSubarrayLength(arr, n, k):
    
    if n == 0:
        return 0
        
    i = 0
    j = -1
    Sum = 0
    length = n+1
    while i<n and j<n:
        if Sum<k:
            j += 1
            if j<n: Sum += arr[j]
        else:
            length = min(length, (j-i+1))
            Sum -= arr[i]
            if i == j:
                j += 1
            i += 1
    return length

if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(smallSubarrayLength(arr, n, k))
        t -= 1