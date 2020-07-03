'''
https://practice.geeksforgeeks.org/problems/length-of-longest-subarray/0
Given an array, return length of the longest subarray of non- negative integers.
Note: Subarray here means a continuous part of the array.
Input:
2
9
2 3 4 -1 -2 1 5 6 3
10
1 0 0 1 -1 -1 0 0 1 0

Output:
4
4
'''

# keep i and j, where i is starting of non-negative window and j is ending, as soon as negative value encountered, we start incrementing both
def length_of_longest_subarray(arr, n):
    i = 0
    j = 0
    maxlen = 0
    count = 0
    while j < n:
        if arr[j] >= 0:
            j += 1
            count += 1
        else:
            maxlen = max(maxlen, count)
            count = 0
            j += 1
            i = j
    maxlen = max(maxlen, count)
    print(maxlen)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        length_of_longest_subarray(arr, n)
        t -= 1