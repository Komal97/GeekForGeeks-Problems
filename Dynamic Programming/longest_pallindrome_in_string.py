'''
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). 
Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. 
Incase of conflict, return the substring which occurs first ( with the least starting index ).
Input:
1
aaaabbaa
Output:
aabbaa
'''

# same as count pallindrome substrings
# just keep start and end of substring
def longest_pallindrome(string, n):
    
    if n == 0 or n == 1:
        print(string)
        return
        
    dp = [[1]*(n) for _ in range(n)]
    start = 0
    end = 0
    maxlen = 1
    for col in range(1, n):
        for row in range(col):
            if row == col-1 and string[row] == string[col]:
                dp[row][col] = 1
                if col-row+1 > maxlen:
                    maxlen = col-row+1
                    start = row 
                    end = col
            elif string[row] == string[col] and dp[row+1][col-1] == 1:
                dp[row][col] = 1
                if col-row+1 > maxlen:
                    maxlen = col-row+1
                    start = row 
                    end = col
            else:
                dp[row][col] = 0
                
    print(string[start:end+1])
    
if __name__ == '__main__':
    t = int(input())
    while t:
        string = input()
        longest_pallindrome(string, len(string))
        t -= 1