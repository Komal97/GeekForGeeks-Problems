'''
https://practice.geeksforgeeks.org/problems/total-decoding-messages/0
A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9.
If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.
Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.
Input:
4
3
123
4
2563
16
4642516137712108
24
675356291270936062618792
Output:
3
2
16
0
'''

def total_decoding(inp, output, count):
    if inp == '':
        #print(output, count)
        count[0] += 1
        return
    
    if len(inp) == 1:
        code = int(inp[0])
        if code == 0:                                           # check for 0 
            return
        else:
            alpha = chr(ord('A') + code - 1)                    # else append length 1 decoded alpha in output
            total_decoding(inp[1:], output + alpha, count)
            
    else:
        code1 = int(inp[0])
        code2 = int(inp[:2])
        if code1 == 0:                                          # if length 1 code is 0
            return
        alpha1 = chr(ord('A') + code1 - 1)
        total_decoding(inp[1:], output + alpha1, count)         # append length 1 decoded alpha in output
        if code2 <= 26:
            alpha2 = chr(ord('A') + code2 - 1)          
            total_decoding(inp[2:], output + alpha2, count)     # append length 2 decoded alpha in output if it is <= 26

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        string = input()
        count = [0]
        total_decoding(string, '', count)
        print(count[0])
        t -= 1