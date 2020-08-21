'''
https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0
Suppose you have N eggs and you want to determine from which floor in a K-floor building you can drop an egg such that it doesn't break. You have to determine the minimum number of attempts you need in order find the critical floor in the worst case while using the best strategy.There are few rules given below. 
An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Input:
2
2 10
3 5

Output:
4
3
'''

def egg_dropping(eggs, floors, memo):
    
    if eggs == 0 or eggs == 1:                    # if 1 egg, then in worst case scario - topmost floor is threshold
        return floors
    elif floors == 0 or floors == 1:
        return floors
        
    if memo[eggs][floors] != -1:
        return memo[eggs][floors]
        
    minans = float('inf') 
    for k in range(1, floors+1):
        temp = 1 + max(egg_dropping(eggs-1, k-1, memo), egg_dropping(eggs, floors-k, memo)) # add current attempt + worst case in both attempts which is asked
        minans = min(minans, temp)
        
    memo[eggs][floors] = minans                                                             # return min of all worst cases
    return minans

if __name__ == '__main__':
    t = int(input())
    while t:
        eggs, floors = list(map(int, input().split()))
        memo = [[-1]*(floors+1) for _ in range(eggs+1)]
        ans = egg_dropping(eggs, floors, memo)
        print(ans)
        t -= 1