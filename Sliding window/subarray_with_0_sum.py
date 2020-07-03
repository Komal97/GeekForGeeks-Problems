'''
https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0
Given an array a[] of N positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.
Input:
2
5
4 2 -3 1 6
5
4 2 0 1 6

Output:
Yes
Yes
'''

# idea is at some point cursum become same as encountered earlier. If 2 sum become same means between them, sum becomes 0
def subarray_with_0_sum(arr, n):
    
    h = {}
    cursum = 0
    for i in range(n):
        cursum += arr[i]
        if cursum in h or cursum == 0:
            return 'Yes'
        else:
            h[cursum] = i
    return 'No'
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(subarray_with_0_sum(arr, n))
        t -= 1