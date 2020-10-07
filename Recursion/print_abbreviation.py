'''
https://www.geeksforgeeks.org/alphanumeric-abbreviations-of-a-string/
You are given a word. You have to generate all abbrevations of that word. The alpha-numeric abbreviation is in the form of 
characters mixed with the digits which is equal to the number of skipped characters of a selected substring.

Input:
pep

Output:
pep
pe1
p1p
p2
1ep
1e1
2p
3
'''

# recursion
# if not consider, count++
# if consider then, if count > 0 then out + count + char and make count = 0 else out + char
def abbreviation(inp, idx, out, count):
    if idx == len(inp):
        if count > 0:
            print(out + str(count))
        else:
            print(out)
        return
    
    if count > 0:
        abbreviation(inp, idx+1, out + str(count) + inp[idx], 0)
    else:
        abbreviation(inp, idx+1, out + inp[idx], count)
    
    abbreviation(inp, idx+1, out, count+1)

string = input()
abbreviation(string, 0, '', 0)

# using bitmasking
# pep = 000
# pe1 = 001
# p1p = 010
# p2  = 011
# 1ep = 100
# 1e1 = 101
# 2p  = 110
# 3   = 111
def print_abbreviation(string, n):
    
    for num in range(1<<n):
        s = ''
        count = 0
        for i in range(n):
            bit = num&(1<<(n-i-1))                              # check bits from right to left
            if bit == 0:
                if count > 0:
                    s += str(count) + string[i]
                    count = 0
                else:
                    s += string[i]
            else:
                count += 1
        print(s + str(count)) if count > 0 else print(s)
    

string = input()
n = len(string)
print_abbreviation(string, n)



