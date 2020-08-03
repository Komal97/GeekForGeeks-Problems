'''
https://practice.geeksforgeeks.org/problems/zero-sum-subarrays/0
You are given an array of integers. You need to print the total count of sub-arrays having their sum equal to 0
Input:
2
6
0 0 5 5 0 0
10
6  -1 -3 4 -2 2 4 6 -12 -7
Output:
6
4

Explanation:
Testcase 2: There are 4 subarrays present whose sum is zero. The starting and ending indices are:
(1,3) (4,5) (1,5) (5,8)
'''

# maintain map {summ: count}
# if summ repeat again means sum of elements between them become 0, count += h[summ] and inc frequency of summ in map
def zerosumsubrray(arr, n):
    
    h = {0: 1}
    count = 0
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ in h:
            count += h[summ]
            h[summ] += 1
        else:
            h[summ] = 1
    
    return count
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(zerosumsubrray(arr, n))
        t -= 1