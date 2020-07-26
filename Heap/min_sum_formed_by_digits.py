'''
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of given array must be used to form the two numbers.
Input
2
6
6 8 4 5 2 3
5
5 3 0 7 4

Output
604
82

Explanation:
Test Case 1
The minimum sum is formed by numbers 
358 and 246
'''

from heapq import heapify, heappop

# min sum is formed if min digit is add with min digit
# direct sort or use min heap and take numbers in first and second
def minSum(arr, n):
    
    heapify(arr)
    first = ''
    second = ''
    val = True
    while len(arr) > 0:
        if val:
            first += str(arr[0])
        else:
            second += str(arr[0])
        val = not val
        heappop(arr)
    print(int(first) + int(second))

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        minSum(arr, n)
        t -= 1