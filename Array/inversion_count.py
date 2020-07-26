'''
https://practice.geeksforgeeks.org/problems/inversion-of-array/0
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Input:
1
5
2 4 1 3 5

Output:
3

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

# use merge sort technique and check each element of first half with second and it is done while merging
def _mergeSort(arr, n):
    temp = [0]*n
    return (mergesort(arr, 0, n-1, temp))
    
def mergesort(arr, s, e, temp):
    count = 0
    if s < e:
        mid = (s+e)//2
        count += mergesort(arr, s, mid, temp)
        count += mergesort(arr, mid+1, e, temp)
        count += merge(arr, s, e, temp)
    return count
 
def merge(arr, s, e, temp):
    mid = (s+e)//2
    i = s
    j = mid+1
    k = s
    count = 0
    while(i<=mid and j<=e):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid-i+1)
            k += 1
            j += 1
    
    while(i<=mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    
    while(j<=e):
        temp[k] = arr[j]
        k += 1
        j += 1
        
    for i in range(s, e+1):
        arr[i] = temp[i]
    return count
    
if __name__ =='__main__':
    t = int(input())
    while(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(_mergeSort(arr, n))
        t -= 1
