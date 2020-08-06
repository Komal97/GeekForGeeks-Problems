'''
https://practice.geeksforgeeks.org/problems/frequency-of-array-elements/0
Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated or can be absent from the array. Your task is to count frequency of all elements from 1 to N.
Note: Expected time complexity is O(n) with O(1) extra space.
Input:
2
5
2 3 2 3 5
4
3 3 3 3

Output:
0 2 2 0 1
0 0 4 0

Explanation:
Testcase 1: Counting frequencies of each array elements, we have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
'''

# since array elements is from 1 to N so same array can be used - O(1) space
# add maxel = n+1 to arr[arr[i]] (consider each number as an index)
# old value = arr[i] % maxel & frequency = arr[i]/maxel 
def count_freq(arr, n):
    
    maxel = n+1
    
    for i in range(n):
        arr[(arr[i]-1)%maxel] += maxel
    
    for i in range(n):
        print(arr[i]//maxel, end = ' ')
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        count_freq(arr, n)
        print()
        t -= 1