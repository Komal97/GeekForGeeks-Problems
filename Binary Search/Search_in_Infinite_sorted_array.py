'''
https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
Find position of element in infinite sorted array

Input: 
9
1 2 3 4 5 6 7 8 9
7

Output:
6
'''

# keep start at 0 and end at 1, loop until arr[end] < key and set start = end and increment end = end * 2
def binary_search(arr, s, e, key):
    
    while e<len(arr) and s<=e:
        mid = (s+e)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            s = mid+1
        else:
            e = mid-1
    return -1

def find_pos(arr, n, key):

    s = 0
    e = 1
    while e<n and key > arr[e]:
        s = e
        e = 2*e
    pos = binary_search(arr, s, e, key)
    print(pos)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    find_pos(arr, n, key)