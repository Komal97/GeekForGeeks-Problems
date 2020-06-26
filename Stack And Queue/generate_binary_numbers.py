'''
https://practice.geeksforgeeks.org/problems/generate-binary-numbers/0
Given a number N. The task is to generate and print all binary numbers with decimal values from 1 to N.

Input:
2
2
5

Output:
1 10
1 10 11 100 101
'''

# use queue
# put 1 in queue, then pop 1 and push 10 and 11
# then pop 10 and push 100 and 101 and so on..
# do this n/2 times because everytime we push 2 elements
from collections import deque
def generateBinary(n):
    if n == 0 or n == 1:
        print(n)
        return
    
    queue = deque(['1'])
    length = n//2
    for i in range(length):
        x = queue.popleft()
        queue.append(x+'0')
        queue.append(x+'1')
        print(x, end = ' ')
    
    if n%2 == 0:
        queue.pop()
    while len(queue) > 0:
        print(queue.popleft(), end = ' ')
    print()

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        generateBinary(n)
        t -= 1