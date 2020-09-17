'''
https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle/0
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​
The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, 
you are the last one remaining and survive.

Example:
Input:
2
3 2
5 3
Output:
3
4

Explanation:
Testcase 1: There are 3 persons so skipping 1 person i.e 1st person 2nd person will be killed. Thus the safe position is 3.
'''

# if n and k is mentions
def josephus(n,k):
    
    if n==1:
        return 1
    
    x = josephus(n-1, k)
    return (x+k-1)%n+1
 
t = int(input())
while t:
    n, k = list(map(int, input().split()))
    ans = josephus(n, k)
    print(ans)
    t -= 1


# if k=2 (killing starting from second)
# then n = 2^x + l (find l)
# ans = 2*l+1
def highestPowerOf2(n):
    i = 1
    while i*2<=n:
        i *= 2
    
    return i

def josephus(n):
    hp = highestPowerOf2(n)
    l = n-hp
    ans = 2*l+1
    return ans 

for i in range(1, 11):
    ans = josephus(i)
    print(ans)
