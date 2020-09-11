'''
https://practice.geeksforgeeks.org/problems/find-sum-of-different-corresponding-bits-for-all-pairs/0
We define f (X, Y) as number of different corresponding bits in binary representation of X and Y. For example, f (2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f (2, 7) = 2.
You are given an array of N integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
Input:
2
2
2 4
3
1 3 5

Output:
4
8

Explanation:
A = [1, 3, 5] 
f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) =
0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
'''

M = 1000000007
def count_total_bits(arr, n):
    
    ans = 0
    for i in range(32):
        unset = 0
        setbit = 0
        for j in range(n):                      # each column of all elements, count set and unset bits
            if (arr[j] & 1):
                setbit += 1
            else:
                unset += 1
            arr[j] >>= 1
        ans = (ans + unset * setbit)%M                # number of pairs = unset*set in a column
    
    ans = (ans * 2)%M
    print(ans)
    
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    count_total_bits(arr, n)
    t -= 1