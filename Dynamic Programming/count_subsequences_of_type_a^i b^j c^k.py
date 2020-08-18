'''
https://practice.geeksforgeeks.org/problems/count-subsequences-of-type-ai-bj-ck/0
Given a string s, the task is to count number of subsequences of the form aibjck, where i >= 1, j >=1 and k >= 1.
Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.
Input:
2
abbc
abcabc
Output:
3
7
Explanation:
Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc, abcc, abc and abc
'''

def count_sub(inp, n):
    
    a = 0                               # consider regex with a+
    ab = 0                              # consider regex with a+b+
    abc = 0                             # consider regex with a+b+c+
    for ch in inp:
        if ch == 'a':                   # if current is 'a'
            a = 2 * a + 1               # then 2 choices(append a' to a or not append) (a, aa', a') + a' can also start string
        elif ch == 'b':                 # if current is 'b'
            ab = 2 * ab + a             # then 2 choices(append b' to ab or not append) + append b to a
        elif ch == 'c':                 # if current is 'c'
            abc = 2 * abc + ab          # then 2 choices(append c' to abc or not append) + append c to ab
    print(abc)
   
if __name__ == '__main__':
    t = int(input())
    while t:
        string = input()
        count_sub(string, len(string))
        t -= 1
    