'''
https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k/0
Given an array of integers and a number K. Write a program to find the maximum sum of a subarray of size K.
Example:
Input:
2
4 2
100 200 300 400
9 4
1 4 2 10 23 3 1 0 20
Output:
700
39
'''

# keep 2 pointers i & j, first find sum of starting window then just keep on increasing i and j by 1
# while i++, subtract arr[i] from sum and while j++, add arr[j] to sum
def max_sum_array_in_window(arr, n, k):
    i = 0
    j = 0
    summ = 0
    while j<k:
        summ += arr[j]
        j += 1
    
    max_sum = summ
    while j<n:
        summ += arr[j]
        summ -= arr[i]
        max_sum = max(max_sum, summ)
        i += 1
        j += 1
    print(max_sum)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
if __name__ == '__main__':
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        max_sum_array_in_window(arr, n, k)
        t -= 1