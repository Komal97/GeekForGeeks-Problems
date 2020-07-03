'''
https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array/0
Given a sorted array arr[] of size N without duplicates, and given a value x. Find the floor of x in given array. 
Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.
Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
-1
1
3
'''

# floor => greatest element smaller than given number
def floor_of_element(arr, n, x):
    
    s = 0
    e = n-1
    ans = -1
    
    while s<=e:
        mid = s + (e-s)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans 

if __name__ == '__main__':
    t = int(input())
    while t:
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(floor_of_element(arr, n, x))
        t -= 1