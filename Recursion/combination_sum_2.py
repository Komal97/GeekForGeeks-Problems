'''
https://practice.geeksforgeeks.org/problems/combination-sum-part-2/0
Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B.
ach number in A may only be used once in the combination.
Note:
All numbers will be positive integers and in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
If there is no combination possible the print "Empty" (without qoutes).
Example:
Input:
2
7
10 1 2 7 6 1 5
8
5
8 1 8 6 8
12

Output:
(1 1 6)(1 2 5)(1 7)(2 6)
Empty
'''

# either include an element in subset or exclude and maintain sum
# when all elements are traversed, then print subsets with given sum
# similar ques - Find subsets from an array having summ equal to given sum.
def findCombination(arr, i, out, target, summ, ans):
    
    if i == len(arr):
        if summ == target:
            ans.add(out)
        return
    
    findCombination(arr, i+1, out + ' ' + str(arr[i]) , target, summ + arr[i], ans) # include element in output and add in sum
    findCombination(arr, i+1, out , target, summ, ans)                              # exclude element 
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        arr.sort()
        ans = set()
        findCombination(arr, 0, '', target, 0, ans)
        if len(ans):
            for a in sorted(ans):
                print('(' + a.strip() + ')', end = "")
            print()
        else:
            print('Empty')
        t -= 1