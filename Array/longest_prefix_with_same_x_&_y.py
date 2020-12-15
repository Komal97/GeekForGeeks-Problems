'''
https://www.geeksforgeeks.org/longest-prefix-contains-number-x-y-array/
Given two positive integers X and Y, and an array arr[] of positive integers. We need to find the longest prefix index which contains an equal number of X and Y. Print the maximum index of largest prefix if exist otherwise print -1.
Examples:

Input : array[] = [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7]
        X = 7 Y = 42
Output : 9
The longest prefix with same number of occurrences  of 7 and 42 is:
7, 42, 5, 6, 42, 8, 7, 5, 3, 6
'''

def findLongestPrefix(arr, n, x, y):
    
    count_x = 0
    count_y = 0

    ans = -1
    for i in range(n):
        if arr[i] == x:
            count_x += 1
        if arr[i] == y:
            count_y += 1
        
        if (count_x != 0) and (count_x == count_y):
            ans = i
    return ans

arr = [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7]
n = len(arr)
x = 7
y = 42
ans = findLongestPrefix(arr, n, x, y)
print(ans)