'''
https://practice.geeksforgeeks.org/problems/adding-array-element/0
Given an array arr[] and an integer K, you have to Add the first two minimum elements of the array until all the elements are greater than or equal to K and find the number of such operations required. 
Input : arr[] = {1 10 12 9 2 3}
        K = 6
Output : 2
First we add (1 + 2), now the new list becomes 3 10 12 9 3, then we add (3 + 3),  now the new list becomes 6 10 12 9, 
Now all the elements in the list are greater than 6. Hence the output is 2 i:e 2 operations are required 
Input : 
2
6 6
1 10 12 9 2 3
5 15
1 2 1 2 2
Output : 
2
-1
'''

from heapq import heappush, heappop, heapify

# if top < k(required min element in heap), pop 2 elements and insert addition
def addArrayElements(arr, n, k):
    cost = 0
    heapify(arr)
    
    while len(arr) > 1:
        if arr[0] < k:
            first = arr[0]
            heappop(arr)
            second = arr[0]
            heappop(arr)
            heappush(arr, first+second)
            cost += 1
        else:
            break
    return cost if arr[0] >=k else -1
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(addArrayElements(arr, n, k))
        t -= 1
        