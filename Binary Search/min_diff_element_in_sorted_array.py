'''
Find element having minimum difference with given element.
Input:
n = 5
arr = [1, 3, 8, 10, 15]
key = 12
'''

# if key present return key
# if not present, nearby element have min difference
# run binary search, if element not found, then start and end will point to neighbours of key where start > end
def binary_search(arr, n, key):
    
    s = 0 
    e = n-1
    while e<len(arr) and s<=e:
        mid = (s+e)//2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            s = mid+1
        else:
            e = mid-1
    a = abs(arr[s] - key)
    b = abs(arr[e] - key)
    return arr[s] if a<b else arr[e]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())
    print(binary_search(arr, n, key))