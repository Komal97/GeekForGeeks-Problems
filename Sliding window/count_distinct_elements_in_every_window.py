'''
https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
Sample Input:
2
7 4
1 2 1 3 4 2 3
3 2
4 1 1

Sample Output:
3 4 4 3
2 1
'''
# keep map with key : value as arr value : index 
# use two pointers to maintain window, i++ and remove value from map and j++ pointer and add value in map
def countDistinct(arr, N, K):
    h = {}
    i = 0
    j = 0
    res = []
    while j<K:
        h[arr[j]] = j
        j += 1
    res.append(len(h))
    
    while j<N:
        h[arr[j]] = j
        if h[arr[i]] <= i:
            del h[arr[i]]
        i += 1
        res.append(len(h))
        j += 1

    return res