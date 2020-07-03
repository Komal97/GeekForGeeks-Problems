'''
https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
Given a sorted array arr[] of size N without duplicates, and given a value x. Find the ceil of x in given array. 
Floor of x is defined as the smallest element K in arr[] such that K is greater than or equal to x.

Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
0
2
3
'''

# ceil => smallest element greater than given number
def ceil_of_element(arr, n, x):
    
    s = 0
    e = n-1
    ans = -1
    
    while s<=e:
        mid = s + (e-s)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1
    return ans 

if __name__ == '__main__':
    t = int(input())
    while t:
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(ceil_of_element(arr, n, x))
        t -= 1