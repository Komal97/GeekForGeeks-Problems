'''
https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring/0
Given a string you need to print the size of the longest possible substring that has exactly k unique characters. If there is no possible substring print -1.
Example
For the string aabacbebebe and k = 3 the substring will be cbebebe with length 7.
Input:
2
aabacbebebe
3
aaaa
1
Output:
7
4
'''

# keep i and j, maintain freq map
# if len(map)>k then i++ until len(map) becomes equal to k, if len(map) == k then find maxlength, 
def uniqueChar(arr, n, k):
    i = 0
    j = 0
    
    h = {}
    maxlen = -1
    while i<n and j<n:
        if arr[j] not in h:
            h[arr[j]] = 1
        else:
            h[arr[j]] += 1
        while i<j and len(h) > k:
            h[arr[i]] -= 1
            if h[arr[i]] == 0:
                h.pop(arr[i])
            i += 1    
        if len(h) == k:
           maxlen = max(maxlen, j-i+1) 
        j += 1
    return maxlen
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        arr = input()
        k = int(input())
        print(uniqueChar(arr, len(arr), k))
        t -= 1