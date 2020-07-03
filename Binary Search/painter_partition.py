'''
https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0
Dilpreet wants to paint his dog- Buzo's home that has n boards with different lengths[A1, A2,..., An]. 
He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.
The problem is to find the minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards, 
say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
Input:
2
2 4
10 10 10 10
2 4
10 20 30 40
Output:
20
60
'''

# similar to allocate min number of pages
def isValid(arr, n, no_of_painter, max_time):
    
    painter = 1
    time = 0
    for num in arr:
        time += num
        if time > max_time:
            time = num
            painter += 1
        if painter > no_of_painter:
            return False
    return True
    
def painter_partition(arr, n, k):
    
    s = 0
    e = 0
    for num in arr:
        s = max(s, num)
        e += num
    
    ans = -1
    while s<=e:
        mid = (s+e)//2
        if isValid(arr, n, k, mid):
            ans = mid
            e = mid-1
        else:
            s = mid+1
    return ans
    
if __name__ == '__main__':
    t = int(input())
    while t:
        k, n = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(painter_partition(arr, n, k))
        t -= 1