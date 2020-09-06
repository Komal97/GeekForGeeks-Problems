'''
https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0
Given an unsorted array of size N of positive integers. One number 'A' from set {1, 2, … N} is missing and one number 'B' occurs twice in array. Find these two numbers.
Input:
2
2
2 2
3 
1 3 3

Output:
2 1
3 2

Explanation:
Testcase 1: Repeating number is 2 and smallest positive missing number is 1.
Testcase 2: Repeating number is 3 and smallest positive missing number is 2.
'''

# using same array, find frequency (same as freq of array elements)
# freq = arr[i]/maxel
# if freq = 2, it is repeated and if freq = 0, it is missed
def findMissingrepeating(arr, n):
    
    maxel = n+1
    
    for i in range(n):
        arr[(arr[i]-1)%maxel] += maxel
    
    miss = -1
    repeat = -1
    for i in range(n):
        if (arr[i]//maxel) == 2:
            repeat = i+1
        if (arr[i]//maxel) == 0:
            miss = i+1
    print(repeat, miss)

# method - 2
# xor all element with other and with 1 to n
# after that we get 2 unique numbers -> now use logic of unique number 2
def findMissingrepeating(arr, n):
    
    xxory = 0
    for num in arr:
        xxory ^= num
    
    for i in range(1, n+1):
        xxory ^= i
    
    rsbm = (xxory&-xxory)
    x = 0
    y = 0
    for num in arr:
        if (num&rsbm)==0:
            x ^= num
        
    for i in range(1, n+1):
        if (i&rsbm)==0:
            x ^= i
    y = xxory^x
    
    for num in arr:
        if num == x:
            print(x, y)
            break
        elif num == y:
            print(y, x)
            break
            
            
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        findMissingrepeating(arr, n)
        t -= 1