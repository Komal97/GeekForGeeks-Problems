'''
https://practice.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string/0
Given a string, the task is to count all palindromic sub-strings present in it.
Input
2
5
abaab
7
abbaeae
Output
3
4
Explanation:
Test Case 1
Input : str = "abaab"
Output: 3
All palindrome substring are : "aba" , "aa" , "baab"
'''

# pallindrome conditions
# 1 char - diagonal elements
# 2 char - both are same or not (if row == col-1 and str1[row] == str1[col])
# 2+ char - if first and last char same and string between them same (str1[row] == str1[col] and dp[row+1][col-1] == 1)
# fill column wise upper triangle
def palindrome(str1, n):
    
    dp = [[1]*(n+1) for _ in range(n+1)]
    count = 0
    for col in range(1, n):
        for row in range(col):
            if row == col-1 and str1[row] == str1[col]:             # if 2 characters and both are equal
                dp[row][col] = 1
                count += 1
            elif str1[row] == str1[col] and dp[row+1][col-1] == 1:  # if first and last char same and string between them same
                dp[row][col] = 1
                count += 1
            else:
                dp[row][col] = 0
                
    print(count)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        str1 = input()
        palindrome(str1, n)
        t -= 1

