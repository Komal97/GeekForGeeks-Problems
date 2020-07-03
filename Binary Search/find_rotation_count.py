'''
https://practice.geeksforgeeks.org/problems/rotation/0
Given a sorted array A of size N. The array is rotated 'K' times. Find the value of 'K'. 
The array may contain duplicate elements.
3
5
5 1 2 3 4
5
1 2 3 4 5
5
2 1 2 2 2
'''

# find small pivot element because before that index array is sorted
# if there are duplicates, for that start++ and end-- until rotated duplicates are not skipped
def rotation(arr, n):
    s = 0
    e = n-1
  
    while s<=e:
        mid = (s+e)//2
        while arr[s] == arr[mid] and s != mid:
            s += 1
        while arr[e] == arr[mid] and e != mid:
            e -= 1
        mid = (s+e)//2
        if mid+1<n and mid-1>=0 and arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            return mid
        elif mid+1<n and arr[mid+1] < arr[mid]:
            return mid+1
        elif arr[e] < arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
            
    # if array is sorted in increasing order
    return 0
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(rotation(arr, n))
        t -= 1