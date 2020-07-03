'''
https://practice.geeksforgeeks.org/problems/maximum-sum-of-subarray-less-than-or-equal-to-x/0
Given an array of integers and a number x. We have to find sum of subarray having maximum sum less than or equal to given value of x.
Input:
2
5
1 2 3 4 5
11
5
2 4 6 8 10
7

Output:
10
6
'''

# keep i=0, j=1 and sum = arr[0]. In while loop if sum<=k then first check for maxsum, then find summ and j++
# this is done so because we want to find the sum, and maxsum sum till now and then advance
# if we keep j = 0, we end up having current element added which make sum > k which is not checked
def subarraysum_lessthan_or_equal_k(arr, n, k):
    i = 0
    j = 1
    maxsum = 0
    summ = arr[0]
    while j < n:
        if summ <= k:
            maxsum = max(maxsum, summ)
            summ += arr[j]
            j += 1
        else:
            while summ>k:
                summ -= arr[i]
                i += 1
    print(maxsum)  
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        subarraysum_lessthan_or_equal_k(arr, n, k)
        t -= 1