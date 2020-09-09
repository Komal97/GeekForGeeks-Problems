'''
https://practice.geeksforgeeks.org/problems/maximum-product-subarray/0
Given an array A that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray such that after taking the mod by 1000000007, the product is maximum.
Input:
3
5
6 -3 -10 0 2
6
2 3 4 5 -1 0 
10
8 -2 -2 0 8 0 -6 -8 -6 -1
Output:
180
120
288
Explanation:
Testcase 1: Subarray with maximum product is 6, -3, -10 which gives product as 180.
'''
 
from math import fmod           # fmod = use to take mod with -ve numbers
M = 1000000007
def max_product(arr, n):
    
    max_prod = arr[0]
    curmax = arr[0]
    curmin = arr[0]
    for i in range(1, n):
        # current window can start from current(arr[i]) or include current in prv window with +ve or include current in prv with -ve
        # -ve because, previously we must have encountered one -ve element which will be minimum and multiplying current -ve, make whole +ve and bigger
        # so maintain max as well as min to handle -ve case
        tempmax = max(arr[i], fmod(curmax*arr[i], M), fmod(curmin*arr[i], M))
        tempmin = min(arr[i], fmod(curmax*arr[i], M), fmod(curmin*arr[i], M))
        curmax = tempmax
        curmin = tempmin
        max_prod = max(max_prod, curmax)
        
    print(int(max_prod))
    
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    max_product(arr, n)
    t -= 1
    
    
