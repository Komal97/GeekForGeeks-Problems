'''
https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed/0
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer mod 10^9 + 7.
Input:
2
3
2
Output:
5
3
Explanation:
Testcase 1: case 5 strings are (000, 001, 010, 100, 101)
Testcse 2:  case 3 strings are (00,01,10)
'''

# just like recursion
# attach 0 and 1 after 0 (for this keep count of prev 0 and prev 1)
# attach only 0 after 1 (for this keep count of prev 0)
M = 1000000007
def generateString(n):
    
    if n == 0:                              # empty string
        print(0)
        return
    if n == 1:                              # string of either 0 or 1 so 2 ways
        print(2)
        return
        
    prev0 = 1                               
    prev1 = 1
    curr0 = 0
    curr1 = 0
    for i in range(2, n+1):
        curr0 = (prev0 + prev1)%M           # attach 0 and 1 to current 0
        curr1 = prev0%M                     # attach 0 to current 1
        prev0 = curr0
        prev1 = curr1
        
    print((curr1+curr0)%M)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        generateString(n)
        t -= 1