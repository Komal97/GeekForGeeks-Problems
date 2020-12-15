'''
https://practice.geeksforgeeks.org/problems/average/0
Given a stream of numbers, print average or mean of the stream at every point.
Input
2
5
10 20 30 40 50
2
12 2

Output
10 15 20 25 30
12 7
'''

# keep sum and find avg
def findAvg(arr, n):
    
    summ = 0
    for i in range(n):
        avg_val = (summ + arr[i])//(i+1)
        summ += arr[i]
        print(avg_val, end = ' ')

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    findAvg(arr, n)
    print()
    t -= 1