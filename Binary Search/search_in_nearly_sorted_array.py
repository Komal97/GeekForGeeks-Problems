'''
https://www.geeksforgeeks.org/search-almost-sorted-array/
Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, 
i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. 
Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].
Input: {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 

Input: {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
'''

# check for mid, mid-1, mid+1 
def almost_sorted_array(arr, n, x):
       
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == x:
            return mid
        elif mid-1 >= s and arr[mid-1] == x:
            return mid-1
        elif mid+1<=e and arr[mid+1] == x:
            return mid+1
        elif arr[mid] < x:
            s = mid + 2
        else:
            e = mid -2

    return -1

if __name__ == '__main__':
    
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(almost_sorted_array(arr, n, x))
        