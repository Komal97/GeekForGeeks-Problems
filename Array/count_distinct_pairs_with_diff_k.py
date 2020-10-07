'''
https://practice.geeksforgeeks.org/problems/count-distinct-pairs-with-difference-k/0
Given an integer array and a non-negative integer k, count all distinct pairs with difference equal to k, i.e., A[ i ] - A[ j ] = k.
Input:
3
5 
1 5 4 1 2
0
3
1 1 1
0
3 
1 5 3
2

Output:
1
1
2
'''

# save array in freq map
# traverse key in map, check key - diff in map then count+=1 else check if diff = 0, then h[key] > 1 then count+=1
from collections import defaultdict
def count_distict(arr, n, diff):
    
    count = 0
    h = defaultdict(int)
    for num in arr:
        h[num] += 1
    
    for key in h:
        if diff == 0:
            if h[key] > 1:
                count += 1
        else:
            if key-diff in h:
                count += 1
    print(count)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        diff = int(input())
        count_distict(arr, n, diff)
        t -= 1