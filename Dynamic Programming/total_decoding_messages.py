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

# recursive
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

# tabulation
def total_decoding(string, n):
    
    dp = [0]*n
    dp[0] = 1 if string[0] != '0' else 0
    
    for i in range(1, n):
        if string[i] == '0' and string[i-1] == '0':             # if both are 0 mean 0 and 00 - don't consider
            dp[i] = 0               
        elif string[i-1] == '0' and string[i] != '0':           # if 02 then 2 is consider so dp[i-1]
            dp[i] = dp[i-1]
        elif string[i-1] != '0' and string[i] == '0':           # if 20 then 20 is consider so dp[i-2] if 2 digit <= 26
            if int(string[i-1:i+1]) <= 26:
                dp[i] = dp[i-2] if i-2 >=0 else 1
            else:
                dp[i] = 0
        else:
            if int(string[i-1:i+1]) <= 26:                      # if 21 so consider 1 (dp[i-1]) and then 21(dp[i-2])
                dp[i] = dp[i-1] + (dp[i-2] if (i-2 >=0 and int(string[i-1:i+1]) <= 26) else 1)
            else:
                dp[i] = dp[i-1]                                 # if 27 so consider 7 only (dp[i-1])
    print(dp[n-1])
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        string = input()
        count = [0]
        total_decoding(string, '', count)
        print(count[0])
        t -= 1