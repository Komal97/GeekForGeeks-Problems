'''
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k/0
Given an array containing N integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.
Input:
3
6 15
10 5 2 7 1 9
6 -5
-5 8 -14 2 4 12
3 6
-1 2 3
Output:
4
5
0
'''

# keep a map of index
# if sum == k means all elements till now become required sum, if sum becomes greater then check for sum-k in map 
def longest_subarray_with_sum_k(arr, n, k):
    maxlen = 0
    summ = 0
    h = {}
    
    for i in range(n):
        summ += arr[i]
        if summ == k:
            maxlen = i+1
        if (summ-k) in h:
            maxlen = max(maxlen, i-h[summ-k])
        if summ not in h: 
            h[summ] = i
    
    print(maxlen)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        longest_subarray_with_sum_k(arr, n, k)
        t -= 1