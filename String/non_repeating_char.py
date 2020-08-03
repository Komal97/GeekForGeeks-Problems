'''
https://practice.geeksforgeeks.org/problems/non-repeating-character/0
Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.
Input :
3
5  
hello
12
zxvczbtxyzvy
6
xxyyzz

Output :
h
c
-1
'''

# create a map of small letters using dict.fromkeys(ascii_lowercase, -1) => initialized with -1 
# if element repeating means index != -1, then h[ch] = -2
# traverse map and find min index -> take constant time
from string import ascii_lowercase
def nonRepeatingChar(arr, n):
    
    h = dict.fromkeys(ascii_lowercase, -1)
    
    for i in range(n):
        if h[arr[i]] == -1:
            h[arr[i]] = i
        else:
            h[arr[i]] = -2
    
    minind = float('inf')
    for ch in h:
        if h[ch] >= 0:
            minind = min(minind, h[ch])
            
    return arr[minind] if minind != float('inf') else -1       

if __name__ == '__main__':
    
    t = int(input())
    while t:
        n = int(input())
        arr = input()
        print(nonRepeatingChar(arr, n))
        t -= 1