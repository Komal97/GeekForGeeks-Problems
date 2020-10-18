'''
https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps/0
Given a string A and integer B, what is maximal lexicographical stringthat can be made from A if you do atmost B swaps.
Input:
3
4
1234567
3
3435335
2
1034

Output:
7654321
5543333
4301
Three swaps can make the input 1234567 to 7654321, swapping 1 with 7, 2 with 6 and finally 3 with 5.
'''

# consider each level for 1 swap
# at each level, we can swap n^2 elements (means each element with all other elements if A[j] > A[i]) 
# keep maxnum formed so far
def largestNum(string, k):
    
    n, exp = len(string), list(string)
    maxnum = string
    
    def generate(exp, k):
        nonlocal maxnum
        
        if int(''.join(exp)) > int(maxnum):
            maxnum = ''.join(exp)
        if k == 0:
            return
        
        for i in range(n-1):
            for j in range(i+1, n):
                if exp[j] > exp[i]:
                    exp[i], exp[j] = exp[j], exp[i]
                    generate(exp, k-1)
                    exp[i], exp[j] = exp[j], exp[i]
                    
    generate(exp, k)
    print(maxnum)
        
    
if __name__ == '__main__':
    t = int(input())
    while t:
        k = int(input())
        string = input()
        largestNum(string, k)
        t -= 1