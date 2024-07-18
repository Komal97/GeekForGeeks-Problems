'''
https://practice.geeksforgeeks.org/problems/decode-the-string/0
An encoded string (s) is given, the task is to decode it. The pattern in which the strings were encoded were as follows
original string: abbbababbbababbbab 
encoded string : "3[a3[b]1[ab]]".
Input:
4
1[b]
3[b2[ca]]
1[a4[bccd]2[c]]
10[geeks]

Output:
b
bcacabcacabcaca
abccdbccdbccdbccdcc
geeksgeeksgeeksgeeksgeeksgeeksgeeksgeeksgeeksgeeks
'''

# push elements in stack and if ']' encounter, pop elements from stack until '[' doesnot arrive
# pop [ and pop n, and repeat the string n number of times. Push back this string again so that it can be used again for outermost bracket
def decode_string(string, n):
    
    stack = []

    i = 0
    while i < n:
        output = ''
        if string[i] != ']':    
            num = 0
            while string[i] >= '0' and string[i] <= '9':            # create a number
                num = num*10 + int(string[i])
                i += 1
            if num != 0:                                            # push number
                stack.append(num)   
            stack.append(string[i])                                 # push all characters
            
        else:                                                       # if closing bracket arrive
            while stack[-1] != '[':                                 # pop until opening bracket encounter
                output = str(stack.pop()) + output                  # append characters
            stack.pop()                                             # pop opening bracket
            times = stack.pop()                                     # pop number
            stack.append(output*times)                              # repeat string n times and push back
        i += 1
    
    print(stack[-1]) if len(stack) > 0 else ''


# using functions        
class Solution:
    def decodedString(self, s):
        
        stack = []
        
        for ch in s:
            if len(stack) == 0 or ch != ']':  # if not closing bracket
                if len(stack) > 0 and ch.isnumeric() and stack[-1].isnumeric(): # if current is number and prev is also number, then append in prev to create a full number
                    stack[-1] += ch
                else:
                    stack.append(ch)   # else append 
            else:
                string = ''
                while stack[-1] != '[':         # pop until opening bracket encounter
                    top = stack.pop()
                    string = top + string       # append characters
                stack.pop()                     # pop opening bracket
                num = stack.pop()               # pop number
                stack.append(string * int(num)) # repeat string n times and push back
        
        return ''.join(stack)