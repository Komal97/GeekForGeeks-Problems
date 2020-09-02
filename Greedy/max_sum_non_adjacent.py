'''
https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array
Input:
2
6
5 5 10 100 10 5
3
1 2 3
Output:
110
4

Explanation:
Testcase1:
5+100+5=110
Testcase2:
1+3=4
'''

# https://practice.geeksforgeeks.org/problems/stickler-theif/0
# current included = prv exc + curr element
# current excluded = max(prev inc, prev exc)
def find_max_loot(arr, n):
    
    inc = arr[0]
    exc = 0
    for i in range(1, n):
        ninc = arr[i] + exc
        nexc = max(inc, exc)
        inc = ninc
        exc = nexc
    return max(inc, exc)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        ans = find_max_loot(arr, 0, n)
        print(ans)
        t -= 1