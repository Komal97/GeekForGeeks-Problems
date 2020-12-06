'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0
Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.
Input:
4
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
4
2 3 0 1
4 
0 1 1 1

Output:
3
2
-1
-1

Explanation:
Testcase 1: 
First jump from 1st element, and we jump to 2nd element with value 3. 
Now, from here we jump to 5h element with value 9 and from here we will jump to last.
'''

# recursive
def minJumps(arr, i, n):
    
    if i >= n-1:
        return 0
    
    min_move = float('inf')
    for j in range(1, arr[i]+1):                            
        move = minJumps(arr, i+j, n)
        if move != -1:
            min_move = min(min_move, move)
            
    return min_move + 1 if min_move != float('inf') else -1
    
# tabulation
def minJumps(arr, n):
    
    dp = [-1]*(n)
    dp[n-1] = 0                                         # n to n is 1 path but 0 move
    
    for i in range(n-2, -1, -1):
        minval = float('inf')   
        for j in range(1, arr[i]+1):                    # find min value of all path jumps from arr[i] using j loop
            if i + j < len(dp) and dp[i+j] != -1:       # check i+j < n and value at i+j != -1 (-1 denotes no path)
                minval = min(minval, dp[i+j])
        if minval != float('inf'):                      # if there is a path, means min != inf
            dp[i] = minval + 1
    
    print(dp[0]) 
    
    
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        minJumps(arr, n)
        t -= 1

# O(n) time, O(1) space
def jump(nums: List[int]):
        
    if len(nums) <= 1:
        return 0
        
    if(nums[0]) == 0:
        return -1
    
    # maintain maximum reachable index from current position
    # maintain maximum possible from current position because if we take maximum steps in 1 jump then total jumps are minimized
    # and total jumps
    maxReachableIndex, possibleSteps, jumps, n = nums[0], nums[0], 1, len(nums)
    
    for i in range(1, n):
        
        if i == n-1:
            return jumps
        
        # maintain maximum reachable index each time
        maxReachableIndex = max(maxReachableIndex, i + nums[i])
        
        # we use a step to get to the current index 
        possibleSteps -= 1
        
        # if steps finish means maximum steps covered in current jump 
        if possibleSteps == 0:
            
            # if both are equal means we get 0 that is why max reachable index is not changed 
            # there is no way to move further
            if i >= maxReachableIndex:
                return -1
        
            # update steps for next round
            possibleSteps = maxReachableIndex - i
            
            # update jump
            jumps += 1
    
    return -1