'''
https://practice.geeksforgeeks.org/problems/number-of-coins/0/
Given a value V. You have to make change for V cents, given that you have infinite supply of each of C{ C1, C2, .. , Cm} valued coins. 
Find the minimum number of coins to make the change.
Output:
Print the minimum number of coins to make the change, if not possible print "-1".
Example:
Input:
1
7 2
2 1

Output:
4

Explanation :
Testcase 1: We can use coin with value 2 three times, and coin with value 1 one times to change a total of 7.
'''

def coinChange(arr, i, n, summ, memo):
    
    if summ == 0:
        return 1
    if i == n and sum != 0:
        return -1
    
    var1 = float('inf')
    if arr[i] <= summ:
        var1 = coinChange(arr, i, n, summ-arr[i], memo)
    var2 = coinChange(arr, i+1, n, summ, memo)
    
    #print(var1, var2)
    
    if var1 <= 0 and var2 <= 0:
        return -1
    elif var1 > 0 and var2 <= 0:
        return var1 + 1
    elif var1 <= 0 and var2 > 0:
        return var2 + 1
    return min(var1, var2) + 1
    
if __name__ == '__main__':
    t = int(input())
    while t:
        summ, n = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        memo = [[-1]*(summ+1) for _ in range(n)]
        print(coinChange(arr, 0, n, summ, memo))
        t -= 1