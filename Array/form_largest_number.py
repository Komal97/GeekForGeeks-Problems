'''
https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
The result is going to be very large, hence return the result in the form of a string.
Input:
2
5
3 30 34 5 9
4
54 546 548 60

Output:
9534330
6054854654
'''

# sort array based on class function (__lt__) overriding
class LargestKey(str):
    def __lt__(x, y):
        return x+y > y+x

def formLargest(arr, n):
    
    arr = sorted(arr, key = LargestKey)
    ans = ''.join(map(str, arr))
    ans = '0' if ans[0] == '0' else ans
    
    print(ans)
    
if __name__ == '__main__':
    t = int(input())
    while(t):
        n = int(input())
        arr = list(map(int,input().split()))
        formLargest(arr, n)
        t -= 1
