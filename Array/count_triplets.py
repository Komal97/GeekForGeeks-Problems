'''
https://www.geeksforgeeks.org/count-triplets-such-that-one-of-the-numbers-can-be-written-as-sum-of-the-other-two/
Given an array A[] of N integers. The task is to find the number of triples (i, j, k) , where i, j, k are indices and (1 <= i < j < k <= N), such that in the set { A_i, A_j, A_k} at least one of the numbers can be written as the sum of the other two.

Examples:
Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are: (1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

Input : A[] = {1, 1, 1, 2, 2}
Output : 6
'''

# if all triplets (not distinct)
def findTriplets(arr, n):

    maxval = max(arr)
    freq = [0]*(maxval+1)
    ans = 0

    for num in arr:
        freq[num] += 1
    
    print(freq)

    # case 1: (0, 0, 0)
    ans += (freq[0] * (freq[0]-1) * (freq[0]-2)//6)
    print(ans)

    # case 2: (0, x, x)
    for i in range(1, maxval+1):
        ans += (freq[0] * freq[i] * (freq[i]-1)//2)
    print(ans)

    # case 3: (x, x, 2x)
    for i in range(1, (maxval+2)//2):
        ans += (freq[i] * (freq[i]-1)//2 * freq[2*i])
    print(ans)

    # case 3: (x, y, x+y)
    for i in range(1, maxval+1):
        for j in range(i+1, maxval+1-i):
            ans += freq[i] * freq[j] * freq[i+j]
    print(ans)

arr = [ 1, 1, 1, 2, 2] 
n = len(arr) 
findTriplets(arr, n)

'''
https://www.geeksforgeeks.org/count-of-triplets-from-the-given-array-such-that-sum-of-any-two-elements-is-the-third-element/?ref=rp
Given an unsorted array arr, the task is to find the count the distinct triplets in which the sum of any two elements is the third element.

Examples:
Input: arr[] = {1, 3, 4, 15, 19}
Output: 2
Explanation:
In the given array there are two triplets such that sum of the any two element is equal to the third element: {{1, 3, 4}, {4, 15, 19}}

Input: arr[] = {7, 2, 5, 4, 3, 6, 1, 9, 10, 12}
Output: 18

Input : arr[] = {1, 1, 1, 2, 2}
Output : 1
'''

# if triplets are distinct
def findTriplets(arr, n):
    
    s = set(arr)
    duplicate = set()
    count = 0
    
    arr.sort()
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) in s and (arr[i], arr[j], arr[i]+arr[j]) not in duplicate:
                count += 1
                duplicate.add((arr[i], arr[j], arr[i]+arr[j]))
    print(count)
    
arr = [ 1, 1, 1, 2, 2] 
n = len(arr) 
findTriplets(arr, n)