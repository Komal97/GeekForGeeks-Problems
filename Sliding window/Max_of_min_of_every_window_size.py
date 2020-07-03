'''
https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size/0
https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/
Given an integer array A[] of size N. The task is to find the maximum of the minimum of every window size in the array.
Input: 
2
7
10 20 30 50 10 70 30
3
10 20 30

Output: 
70 30 20 10 10 10 10 
30 20 10

Explaination:
Testcase 1:
First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10}, {70} and {30}. Maximum of these minimums is 70.
Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10}, and {30}. Maximum of these minimums is 30.
Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. Maximum of these minimums is 20.
'''

def next_smaller(arr, n):
    stack = []
    nse = [0]*n
    
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            nse[i] = n
        else:
            nse[i] = stack[-1]
        stack.append(i)
    return nse
    
def previous_smaller(arr, n):
    stack = []
    pse = [0]*n
    
    for i in range(n):
        while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]
        stack.append(i)
    return pse
    
def find_max_in_min_window(arr, n):
    
    nse = next_smaller(arr, n)
    pse = previous_smaller(arr, n)
    
    ans = [0]*(n+1)
    for i in range(n):
        length = nse[i] - pse[i] - 1
        ans[length] = max(ans[length], arr[i])
    
    
    for i in range(n-1, 0, -1):
        ans[i] = max(ans[i], ans[i+1])
            
    print(*ans[1:], sep = " ")
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n= int(input())
        arr = list(map(int, input().split()))
        find_max_in_min_window(arr, n)
        t -= 1