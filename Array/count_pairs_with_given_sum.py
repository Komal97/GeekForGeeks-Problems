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

# in first iter - create frequency map and in sec iter - find pairs
def count_pair(arr, n, x):
    
    h = {}
    count = 0
    for num in arr:
        if num in h:
            h[num] += 1
        else:
            h[num] = 1
    
    for num in arr:
        if x-num in h:                  # if other element found then add other element frequency because it will pair with all
            count += h[x-num]
        
        if x-num == num:                # if sum-num is itself, then count--  it exclude itself from count and make pair with other same element
            count -= 1
    return count//2                     # (x, y) and (y, x) are counted so they are counted twice
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(count_pair(arr, n, x))
       
        t -= 1