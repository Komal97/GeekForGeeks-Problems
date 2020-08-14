'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions/0    
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. 
It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
Input:
1
4 3
heap pea 

Output:
3 (2 deletion, 1 insertion)
'''

# find LCS length
# always delete from first str1 so no. of deletions = l1 - LCS
# number of insertions in str1 = l2 - LCS
def min_insert_delete(str1, str2, l1, l2):
    
    dp = [[0]*(l2+1) for _ in range(l1+1)]
    
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcsLength = dp[l1][l2]
    ans = (l1-lcsLength) + (l2-lcsLength)      
    print(ans)

if __name__ == '__main__':
    t = int(input())
    while t:
        l1, l2 = list(map(int, input().split()))
        str1, str2 = input().split()
        min_insert_delete(str1, str2, l1, l2)
        t -= 1