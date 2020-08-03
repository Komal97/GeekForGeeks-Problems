'''
https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion/0
Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. 
The relative order of elements is same in the output i.e you have to iterate on the original array only.
Input:
2
7
4 3 7 8 6 2 1
4
1 4 3 2
Output:
3 7 4 8 2 6 1
1 4 2 3
'''

# 0th position element should be smaller than next element
# 1st position elements should be greater than next element
# maintain flag and do it for alternate positions
def zigzag(arr, n):
    
    flag = True
    for i in range(n-1):
        
        if flag:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
           
        flag = not flag
        
    print(*arr, sep = ' ')

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        zigzag(arr, n)
        t -= 1