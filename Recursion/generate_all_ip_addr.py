'''
https://practice.geeksforgeeks.org/problems/generate-ip-addresses/1
Given a string S containing only digits, Your task is to complete the function genIp() which returns a vector containing all possible combination of valid IPv4 ip address and takes only a string S as its only argument.
For string 11211 the ip address possible are 
1.1.2.11
1.1.21.1
1.12.1.1
11.2.1.1
Expected Time Complexity: O(N * N * N * N)
Expected Auxiliary Space: O(N * N * N * N)

Example(To be used only for expected output):
Input
4
11211
67535629
255255255255
50361

Output
1.1.2.11
1.1.21.1
1.12.1.1
11.2.1.1
67.53.56.29
255.255.255.255
5.0.3.61
5.0.36.1
50.3.6.1
'''

# consider digits, keep dotcount till 4. We have 3 options for digits:
# consider 1 digit and add (.)
# consider 2 digit & cannot start from 0 and add(.)
# consider 3 digit & check it should be less than 256 & cannot start from 0 and add (.)
def Ipaddr(inp, out, dotcount, ans):
    if inp == '':
        if dotcount == 4:
            ans.append(out[:-1])
        return
    
    Ipaddr(inp[1:], out + inp[0] + '.', dotcount+1, ans)
    if len(inp) >= 2 and inp[0] > '0':
        Ipaddr(inp[2:], out + inp[:2] + '.', dotcount+1, ans)
    if len(inp) >= 3 and inp[:3] <'256' and inp[0] > '0':
        Ipaddr(inp[3:], out + inp[:3] + '.', dotcount+1, ans)

def genIp(s):
    
    ans = []
    Ipaddr(s, '', 0, ans)
    return ans