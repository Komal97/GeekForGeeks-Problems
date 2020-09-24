'''
https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
Note: Expected solution in O(n) time using constant extra space.
Input:
2
5
1 2 3 4 5
5
0 -10 1 3 -20
Output:
6
2
'''

# use Index to keep check of smallest positive

# Method - 1
# move all -ve numbers to starting and remove them from array
# then mark visited places as -ve. It number on any index is +ve means that +ve number is not found
def segreggate(arr, n):
    i = 0
    for j in range(n):
        if arr[j] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i

def missingNumber(arr,n):
    
    ind = segreggate(arr, n)
    arr = arr[ind:]
    
    n = len(arr)
    for i in range(n):
        if abs(arr[i])-1 < n and arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    
    for i in range(n):
        if arr[i] > 0:
            return i+1
    return n+1

# Method - 2
# ignore num <= 0 or > n
# put val at arr[val] & save arr[val] as nextval and keep on doing this until val<0 or val>0 and arr[val]!=val
def missingNumber(arr,n):
    
    if n == 0:
        return 1
    
    for i in range(n):
        if arr[i] <= 0 and arr[i] > n:
            continue
        val = arr[i]
        
        while val > 0 and  val <= n and arr[val-1] != val:
            nextval = arr[val-1]
            arr[val-1] = val
            val = nextval
    
    for i in range(n):
        if arr[i] != i+1:
            return i+1
    return n+1

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split().strip()))
        print(missingNumber(arr, n))
        t -= 1