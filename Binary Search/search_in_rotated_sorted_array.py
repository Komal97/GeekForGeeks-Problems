'''
https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. 
The task is to find the index of the given element K in the array A.
Input:
3
9
5 6 7 8 9 10 1 2 3
10
3
3 1 2
1
4
3 5 1 2
6

Output:
5
1
-1
'''

# find minimum element, before that array is sorted and after that also array is sorted
# so we call binary search on both sides and return our index accordingly
def binary_search(arr, s, e, key):
    
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            s = mid+1
        else:
            e = mid-1
    return -1

def find_min_index(arr, n):
    
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if mid-1>=0 and mid+1<n and arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
            return mid
        elif mid+1<n and arr[mid] > arr[mid+1]:
            return mid+1
        elif arr[e] < arr[mid]:
            s = mid + 1
        else:
            e = mid -1 
    return 0
    
def search(arr, n, key):
    
    min_index = find_min_index(arr, n)
    left = binary_search(arr, 0, min_index-1, key)
    if left != -1:
        return left
    right = binary_search(arr, min_index, n-1, key)
    return right 
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        key = int(input())
        print(search(arr, n, key))
        t -= 1