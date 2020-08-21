'''
https://practice.geeksforgeeks.org/problems/edit-distance/0
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.
Insert, Remove, Replace
All of the above operations are of cost=1. Both the strings are of lowercase.
Input:
1
4 5
geek gesek
Output:
1
Explanation:
Testcase 1: One operation is required to make 2 strings same i.e. removing 's' from str2.
'''

def edit_distance(str1, n, str2, m):
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # initialization of empty string
    for i in range(1, n+1):
        dp[i][0] = i
        
    for j in range(1, m+1):
        dp[0][j] = j
    
    # calculate cost
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:                     # if character equal, no change 
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i][j] means replace, dp[i-1][j] means delete, dp[i][j-1] means insert
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                
    print(dp[n][m])


if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = list(map(int, input().split()))
        str1, str2 = input().split()
        edit_distance(str1, n, str2, m)
        t -= 1