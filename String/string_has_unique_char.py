'''
https://www.geeksforgeeks.org/determine-string-unique-characters/
Given a string, Determine if the string has all unique characters.

Examples :

Input : abcd10jk
Output : true

Input : hutg9mnd!nk9
Output : false
'''

# method - 1, maintain hashmap, set for keeping track of already visited character -> space o(n)
# method - 2, maintain a 32 bit number, where each bit represents each character -> valid for a-z characters only
def uniquechar(exp):

    # set 32 bit index number 
    checker = 0
    for ch in exp:
        # get character index
        bitAtIndex = ord(ch) - ord('a')
        # check if it is already set
        if (checker & (1<<bitAtIndex)) > 0:
            return False
        # if not set, then continue and set bit
        checker = checker | (1<<bitAtIndex)
    return True

if __name__ == '__main__':
    exp = input()
    print(uniquechar(exp))
