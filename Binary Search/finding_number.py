'''
https://practice.geeksforgeeks.org/problems/finding-number/0
An array is called Bitonic if it is comprises of an increasing sequence of integers followed immediately by a decreasing sequence of integers.
Given a bitonic array A of N distinct integers. Find a element X in i
Input:
1
5
1 2 7 4 3
2
Output:
1

Explanation:
Testcase 1: 2 is found at index 1 in the given array.
'''

# find peak element
# before peak, array is sorted in increasing so call binary search
# after peak, array is sorted in decreasing so call binary search
def binarysearch_asc(arr, s, e, key):
    
    while s>=0 and s<=e:
        mid = s + (e-s)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return -1

def binarysearch_desc(arr, s, e, key):
    
    while e < n and s<=e:
        mid = s + (e-s)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            s = mid + 1
        else:
            e = mid - 1
    return -1
    
def find_peak(arr, n):
    s = 0
    e = n-1
    
    while s<=e:
        mid = s+ (e-s)//2
        if mid > 0 and mid < n-1:
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                s = mid + 1
            else:
                e = mid - 1
        elif mid == 0:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        elif mid == n-1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2

def find_number(arr, n, key):
    
    peak = find_peak(arr, n)
    left = binarysearch_asc(arr, 0, peak-1, key)
    right = binarysearch_desc(arr, peak, n-1, key)
    
    if left == -1 and right == -1:
        return -1
    elif left == -1:
        return right
    return left
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        key = int(input())
        print(find_number(arr, n, key))
        t -= 1
