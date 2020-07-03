'''
https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0
Given a string S and text T. Output the smallest window in the string S having all characters of the text T. Both the string S and text T contains lowercase english alphabets.
Input:
2
timetopractice
toc
zoomlazapzo
oza

Output:
toprac
apzo
'''

def smallest_windows_with_char_of_other_string(S, T):
    
    result = ''
    if S == '' or T == '':
        return -1
    
    # keep a map for string T 
    ht = {}
    for ch in T:
        if ch not in ht:
            ht[ch] = 1
        else:
            ht[ch] += 1
    
    
    # it keeps count of characters in S matches with T with same frequency
    lettercount = 0
    # keep a map for string from which substring has to be find (window map)
    hs = {}
    # denotes window starting
    i = 0
    minlen = len(S)+1
    for j in range(len(S)):
        ch = S[j]
        # if current character is in T then add it in window map
        if ch in ht:
            if ch not in hs:
                hs[ch] = 1
            else:
                hs[ch] += 1
            # if keep character count of S which matches with T with same frequency 
            if hs[ch] <= ht[ch]:
                lettercount += 1
        
        # lettercount become equal to T means we have found substring
        if lettercount == len(T):
            # starting removing characters from S which are not relevant or extra characters
            while S[i] not in hs or hs[S[i]] > ht[S[i]]:
                if S[i] in hs:
                    hs[S[i]] -= 1
                i += 1
            # now find minimum length and then substring
            length = j-i+1
            if length < minlen:
                minlen = length
                result = S[i: i+length]
            
            # after finding substring, we further shrink our window for further processing
            hs[S[i]] -= 1
            lettercount -= 1
            i += 1
            
    return result if result != '' else -1

if __name__ == '__main__':
    t = int(input())
    while t:
        S = input()
        T = input()
        print(smallest_windows_with_char_of_other_string(S, T))
        t -= 1