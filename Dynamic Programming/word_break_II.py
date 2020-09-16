'''
https://practice.geeksforgeeks.org/problems/word-break-part-2/0
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, given s = "snakesandladder",
dict = ["snake", "snakes", "and", "sand", "ladder"].
A solution is ["snakes and ladder", "snake sand ladder"].
Exapmle:
Input:
1
5
lr m lrm hcdar wk
hcdarlrm
Output:
(hcdar lr m)(hcdar lrm)
'''

# recursion => check current prefix substring and check further is also present in dictionary
def word_break(dictionary, string, ans):
    if string == '':
        print('(' + ans.strip() + ')', end = '')
        return
    
    for i in range(len(string)):
        if string[:i+1] in dictionary:                                         
            word_break(dictionary, string[i+1:], ans + string[:i+1] + ' ')
            
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        dictionary = input().split()
        string = input()
        word_break(dictionary, string, '')
        print()
        t -= 1