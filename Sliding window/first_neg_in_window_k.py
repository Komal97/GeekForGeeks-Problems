'''
https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k/0
Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.
Input:
2
5
-8 2 3 -6 10
2
8
12 -1 -7 8 -15 30 16 28
3

Output:
-8 0 -6 -6
-1 -1 -7 -15 -15 0
'''

def first_negative_in_window(arr, n, k):
    
    i = 0   # window start pointer
    for j in range(k-1, n):  
        # loop until start < end of window and (current element is positive or end-start >= k) and start++
        while i<j and (arr[i] > 0 or i <= j-k):
            i += 1
        # if element at window start is negative then print it else 0
        neg = arr[i] if arr[i] < 0 else 0
        print(neg, end = " ")                                                                                                                                                                                         
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        first_negative_in_window(arr, n, k)
        print()
        t -= 1