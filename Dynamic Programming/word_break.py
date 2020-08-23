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

# create a dictionary of given
# check presence of substring each time in dictionary, if found, start = end + 1 and end += 1
from collections import Counter
def word_break(dictionary, string, n):
    
    h = Counter(dictionary)
    start = 0
    end = 0
    for i in range(len(string)):
        if string[start: end+1] in h:
            start = end+1
            end = end+1
        else:
            end = end+1
            
    print(int(string[start:end+1] in h)) if start < len(string) else print(1)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        dictionary = input().split()
        string = input()
        word_break(dictionary, string, n)
        t -= 1