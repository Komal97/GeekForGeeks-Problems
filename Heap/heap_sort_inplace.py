'''
https://practice.geeksforgeeks.org/problems/heap-sort/1
Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() which are used to implement Heap Sort.
Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)
Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10
'''

# for ascending order - build maxheap
# for descending order - build minheap

# heapify function for maxheap
def heapify(arr, n, i):

    leftchild = (2*i)+1
    rightchild = (2*i)+2
    
    maxindex = i
    if leftchild < n and arr[leftchild] > arr[i]:
        maxindex = leftchild
    
    if rightchild < n and arr[rightchild] > arr[maxindex]:
        maxindex = rightchild
    
    if maxindex != i:
        arr[i], arr[maxindex] = arr[maxindex], arr[i]
        heapify(arr, n, maxindex)

# arrange array to build heap according to maxheap
def buildHeap2(arr, n):
    
    # we start heapifying from last second level (exclude leaf nodes)
    # O(n) time
    for i in range((n-1)//2, -1, -1):
        heapify(arr, n, i)
    
def buildHeap(arr,n):
   
    buildHeap2(arr, n)
    # elements in the last are sorted   
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)