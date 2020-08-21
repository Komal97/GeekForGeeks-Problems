'''
https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game/0
You are given an array A of size N. The array contains integers and is of even length. The elements of the array represent N coin of values V1, V2, ....Vn. 
You play against an opponent in an alternating way. In each turn, a player selects either the first or last coin from the row, 
removes it from the row permanently, and receives the value of the coin. You need to determine the maximum possible amouint of money you can win if you go first.
Input:
2
4
5 3 7 10
4
8 15 3 7
Output:
15
22

Explanation:
Testcase1: The user collects maximum value as 15(10 + 5)
Testcase2: The user collects maximum value as 22(7 + 15)
'''

# if first player turn then choose arr[i] and in this case second player can choose j or i+1 and call accordingly & find min of 2 calls
# if sec player turn then choose arr[j] and in this case first player can choose i or j-1 so call accordingly & find min of 2 calls
# choose min because current player choose so that other players output is minimized
# return max of both player     
def optimal_game(arr, i, j, memo):
    if i > j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    first_player = arr[i] + min(optimal_game(arr, i+2, j,memo), optimal_game(arr, i+1, j-1,memo))
    second_player = arr[j] + min(optimal_game(arr, i, j-2,memo), optimal_game(arr, i+1, j-1,memo))
    
    memo[i][j] = max(first_player, second_player)
    return memo[i][j]
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        memo = [[-1]*(n) for _ in range(n)]
        ans = optimal_game(arr, 0, n-1, memo)
        print(ans)
        t -= 1