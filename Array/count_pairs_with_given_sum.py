'''
https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0
Given an array of integers, and an integer  ‘K’ , find the count of pairs of elements in the array whose sum is equal to 'K'.
Input
2
4 6
1  5  7 1
4 2
1 1 1 1
Output
2
6
'''

# create a freq map
# while adding in map, check x-num in h, if present then add h[x-num] into count and add current element in map
from collections import defaultdict
def count_pair(arr, n, x):
    
    h = defaultdict(int)
    count = 0
    
    for num in arr:
        if x-num in h:
            count += h[x-num]
        h[num] += 1

    return count

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(count_pair(arr, n, x))
       
        t -= 1