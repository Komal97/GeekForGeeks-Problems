'''
https://practice.geeksforgeeks.org/problems/stock-span-problem/0
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price 
for all n days. The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the current day is less than or equal to its price on the given day.
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80

Output:
1 1 1 2 1 4 6
1 1 2 4 5 1
'''
# keep stack of index
# pop out index until we get less elements than current and then get total days by subtracting index of currect element and top element
# if top element is greater, we push element
# intuition is, if top is less, then element less than that is popped out 
def stock_span(arr, n):
    if n == 1:
        print(1)
        return 
    
    stack = [-1]
    for i in range(n):
        if stack[-1] == -1 or arr[stack[-1]] > arr[i]:
            stack.append(i)
            print(1, end = ' ')
        else:
            while stack[-1] != -1 and arr[stack[-1]] <= arr[i]:
                stack.pop()
            print(i-stack[-1], end = ' ')
            stack.append(i)
            

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        stock_span(arr, n)
        print()
        t -= 1