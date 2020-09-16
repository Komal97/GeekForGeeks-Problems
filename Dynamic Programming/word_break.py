'''
https://practice.geeksforgeeks.org/problems/word-break/0
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}
Input:  ilike
Output: Yes
The string can be segmented as "i like".
Input:
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike
Output:
1
0
'''
# recursion => check current prefix substring and check further is also present in dictionary
def word_break(dictionary, string):
    if string == '':
        return 1
    
    for i in range(len(string)+1):
        if string[:i] in dictionary:                            
            if(word_break(dictionary, string[i:])):
                return 1
    return 0

# memoized
from collections import Counter
def wordBreakDp(string, wordDict, dp, idx):
    
    if idx == len(string):                                      # if string is find completely in dictionary
        return 1
    
    if dp[idx] != -1:                                           # dp[idx] stores starting index of string after which string is equal or not
        return dp[idx]
    
    for i in range(idx, len(string)):
        if string[idx:i+1] in wordDict:                         # if current to i is present in dict then check for i+1
            dp[idx] = wordBreakDp(string, wordDict, dp, i+1)
            if dp[idx] == 1:
                return 1
    
    dp[idx] = 0
    return dp[idx]
    
def word_break(dictionary, string):

    h = Counter(dictionary)
    dp = [-1]*(len(string)+1)
    ans = wordBreakDp(string, h, dp, 0)
    return ans

t = int(input())
while t:
    n = int(input())
    dictionary = input().split()
    string = input()
    ans = word_break(dictionary, string)
    print(ans)
    t -= 1
