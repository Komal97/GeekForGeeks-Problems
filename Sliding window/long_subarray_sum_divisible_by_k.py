'''
https://practice.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k/0
Given an array containing N integers and a positive integer K. The task is to find the length of the longest sub array with sum of the elements divisible by the given value K.
Input:
2
6 3
2 7 6 1 4 5
7 3
-2 2 -5 12 -11 -1 7
Output:
4
5

Explanation:

Input : A[] = {2, 7, 6, 1, 4, 5}, K = 3
Output : 4
The subarray is {7, 6, 1, 4} with sum 18,
which is divisible by 3.
'''
# we are storing and checking sum%k
# means if at 2 places sum%k become same, it means between them sum%k become 0
# similar to pigeonhole concept used in divisible subarray
def long_subarray_sum_divisible_by_k(arr, n, k):
    
    maxlen = 0
    summ = 0
    h = {}
    for i in range(n):
        summ += arr[i]
        mod = summ % k
        if mod == 0:
            maxlen = i+1
        if mod in h:
            maxlen = max(maxlen, i-h[mod])
        else: 
            h[mod] = i
    print(maxlen)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        long_subarray_sum_divisible_by_k(arr, n, k)
        t -= 1