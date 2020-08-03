'''
https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/0
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
Input:
2
7
2 6 1 9 4 5 3
7
1 9 3 10 4 20 2

Output:
6
4

Explanation:
Testcase 1:  The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
'''

# add all elements in set
# check num-1 in set, if not present it means it becomes the start of sequence
# using while check consec numbers and count++, then find maxcount
def longestConsecSubseq(arr, n):
    maxcount = 0
    s = set()
    for num in arr:
        s.add(num)
        
    for num in arr:
        if num-1 not in s:
            count = 0
            x = num
            while x in s:
                count += 1
                x += 1
            maxcount = max(maxcount, count)
            
    return maxcount
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(longestConsecSubseq(arr, n))
        t -= 1