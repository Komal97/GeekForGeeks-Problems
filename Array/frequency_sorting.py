'''
https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.
Input:
2
5
5 5 4 6 4
5
9 9 9 2 5

Output:
4 4 5 5 6
9 9 9 2 5
'''

# create a map of frequency and sort it
# sorting can be done using inbuild sort or heap also
def frequencySort(arr, n):
    
    h = {}
        
    for num in arr:
        if num not in h:
            h[num] = 1
        else:
            h[num] += 1
    
    ans = sorted(h.items(), key = lambda x: x[1], reverse = True)
    
    for el, freq in ans:
        while freq:
            print(el, end = ' ')
            freq -= 1
    
if __name__ == '__main__':
    
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        frequencySort(arr, n)
        print()
        t -= 1