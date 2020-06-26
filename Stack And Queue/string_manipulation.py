'''
https://practice.geeksforgeeks.org/problems/string-manipulation/0
Tom is a string freak. He has got sequences of  n words to manipulate. If in a sequence, two same words come together then he’ll destroy each other. He wants to know the number of words left in the sequence after this pairwise destruction.
Input:
2
5
ab aa aa bcd ab
4
tom jerry jerry tom

Output:
3
0

Explanation:

Test Case 1: ab aa aa bcd ab
After the first iteration, we'll have: ab bcd ab
We can't further destroy more strings and hence we stop and the result is 3. 

Test Case 2: tom jerry jerry tom
After the first iteration, we'll have: tom tom
After the second iteration: 'empty-array' 
Hence, the result is 0. 
'''

# if coming word and last word is same then pop from stack else keep pushing words into stack
def counter(explist, n):
    
    stack = []
    for word in explist:
        if len(stack) == 0 or stack[-1] != word:
            stack.append(word)
        else:
            stack.pop()
    return len(stack)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        exp = input()
        explist = exp.split()
        print(counter(explist, n))
        t -= 1