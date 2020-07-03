'''
Given a sorted array A of size N and a number X, you need to find the number of occurrences of X in A.
Input:
2
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
Output:
4
-1
'''

# find the element, then call on first part for finding first occurance, and call on second for finding last occurance
def lowest_occurrence(arr, s, e, x):
    
    ans = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == x:
            ans = mid
            e = mid-1
        elif arr[mid] < x:
            s = mid + 1
        else:
            e = mid-1
    return ans

def upper_occurrence(arr, s, e, x):
    
    ans = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == x:
            ans = mid
            s = mid+1
        elif arr[mid] < x:
            s = mid + 1
        else:
            e = mid-1
    return ans
    
def number_of_occurances(arr, n, x):
    
    s = 0
    e = n-1
    ans = -1
    l = -1
    u = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == x:
            ans = mid
            l = lowest_occurrence(arr, 0, mid-1, x)
            u = upper_occurrence(arr, mid+1, e, x)
            break
        elif arr[mid] < x:
            s = mid+1
        else:
            e = mid-1
    
    if ans == -1:
        return -1
    elif l == -1 and u == -1:
        return 1
    elif l == -1:
        return u-mid+1
    elif u == -1:
        return mid-l+1
    return u-l+1
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(number_of_occurances(arr, n, x))
        t -= 1