'''
https://practice.geeksforgeeks.org/problems/subsets/0
Given an array of integers that might contain duplicates, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Input:
2
3
1 2 2
4
1 2 3 3

Output:
()(1)(1 2)(1 2 2)(2)(2 2)
()(1)(1 2)(1 2 3)(1 2 3 3)(1 3)(1 3 3)(2)(2 3)(2 3 3)(3)(3 3)
'''

# either include or exclude an element in output 
def printSubsets(arr, i, n, output, ans):
    
    if i == n:
        ans.add(output)
        return
    
    printSubsets(arr[1:], i+1, n, output + ' ' +str(arr[0]), ans)
    printSubsets(arr[1:], i+1, n, output, ans)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        
        ans = set()
        printSubsets(arr, 0, n, '', ans)
 
        for a in sorted(ans):
            print('(' + a.strip() + ')', end = '')
        print()
        t -= 1