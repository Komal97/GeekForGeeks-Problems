'''
https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring/0
Given a string, find the length of the longest substring without repeating characters. For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6.
Input:
2
geeksforgeeks
qwertqwer

Output:
7
5
'''

def longest_substring_in_window(string):
    
    start = 0
    seen = {}
    max_length = 0
    
    # keep a starting ptr for starting of window and end pointer keeps on increasing & find maxlength
    # when already traversed element is encountered, then we see whether duplicate character occur after start means in current window or before start means prv window
    for end in range(len(string)):
        if string[end] in seen:
            start = max(start, seen[string[end]]+1)
        seen[string[end]] = end
        max_length = max(max_length, end-start+1)
    return max_length

if __name__ == '__main__':
    t = int(input())
    while t:
        string = input()
        print(longest_substring_in_window(string))
        t -= 1