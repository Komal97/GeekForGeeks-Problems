'''
https://practice.geeksforgeeks.org/problems/combination-sum/0s
Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B. The same repeated number may be chosen from A unlimited number of times.
Note:
1. All numbers will be positive integers and in non-descending order. 
2. The combinations themselves must be sorted in ascending order.
Input:
3
4
7 2 6 5
16
11
6 5 7 1 8 2 9 9 7 7 9
6
4
2 4 6 8
8

Output:
(2 2 2 2 2 2 2 2)(2 2 2 2 2 6)(2 2 2 5 5)(2 2 5 7)(2 2 6 6)(2 7 7)(5 5 6)
(1 1 1 1 1 1)(1 1 1 1 2)(1 1 2 2)(1 5)(2 2 2)(6)
(2, 2, 2, 2)(2, 2, 4)(2, 6)(4, 4)(8)
'''

# consider  j = i to n index from array and and call recursion on j
# ex - consider i = 0 and recusion on 0 to n and find all possibilties until sum = target and return if sum > target 
# then consider i = 1 and recursion on 1 to n and so on..
def findCombination(arr, i, n, output, target, summ, ans):
    
    if summ > target:
        return

    if summ == target:
        ans.add(output.strip())
        return

    for j in range(i, n):                         # keep calling on first index through j until base cond doesn't hit
        findCombination(arr, j, n, output + ' ' + str(arr[j]), target, summ+arr[j], ans)
        
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        arr.sort()
        ans = set()
                                    
        findCombination(arr, 0, n, '', target, 0, ans)      # send first index
            
        if len(ans):
            for a in sorted(ans):
                print('(' + a + ')', end = '')
            print()
        else:
            print('Empty')
        t -= 1