'''
https://practice.geeksforgeeks.org/problems/smallest-distant-window/0
Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca”.
Input:
2
aabcbcdbca
aaab

Output:
4
2
'''

# logic same as that of 'window in string with all charcaters of other string'
# here same string behave as 2 strings
def smallest_distinct_window(s):
    
    if s == '':
        return -1
    
    hset = set()
    for ch in s:
        hset.add(ch)
        
    i = 0
    lettercount = 0
    window = {}
    minlength = len(S) + 1
    for j in range(len(s)):
        ch = s[j]
        if ch in hset:
            if ch not in window:
                window[ch] = 1
            else:
                window[ch] += 1
        if window[ch] == 1:
            lettercount += 1
            
        if lettercount == len(hset):
            while S[i] not in hset or window[S[i]] > 1:
                if S[i] in window:
                    window[S[i]] -= 1
                i += 1
            minlength = min(minlength, j-i+1)
            window[S[i]] -= 1
            lettercount -= 1
            i += 1
    return minlength
    
if __name__ == '__main__':
    t = int(input())
    while t:
        S = input()
        print(smallest_distinct_window(S))
        t -= 1