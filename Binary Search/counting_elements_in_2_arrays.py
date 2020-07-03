'''
https://practice.geeksforgeeks.org/problems/counting-elements-in-two-arrays/1
Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements less than or equal to it in array arr2[].
Expected Time Complexity: O((m + n) * log n).
Expected Auxiliary Space: O(1).
Input:
2
6 6
1 2 3 4 7 9
0 1 2 1 1 4
5 7
4 8 7 5 1
4 48 3 0 1 1 5

Output:
4 5 5 6 6 6 
5 6 6 6 3
'''

# sort second array and for every element in arr1, search element in aa2 using binary search
def search(arr, n, key):
    s = 0
    e = n-1
    
    ans = -1
    while s<=e:
        mid = s+(e-s)//2
        if arr[mid] == key:
            ans = mid
            s = mid+1
        elif arr[mid] < key:
            s = mid+1
        else:
            e = mid-1
    return e if ans == -1 else ans
    
def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    arr2.sort()
    
    res = []
    for num in arr1:
        if num >= arr2[n2-1]:
            res.append(n2)
        else:
            ind = search(arr2, n2, num)
            res.append(ind+1)
    return res