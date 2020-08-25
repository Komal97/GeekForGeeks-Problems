'''
https://practice.geeksforgeeks.org/problems/next-greater-number-set-digits/0 
Given a number n, find the smallest number that has same set of digits as n and is greater than n. 
If x is the greatest possible number with its set of digits, then print “not possible”.
Input
5
17422
19170
134
143
431

Output
21247
19701
143
314
not possible
'''

# move from right to left
# if inc -> 134 then swap last 2 i.e. 143
# if dec -> means no larger number can be formed -> 431
# Example - 17422 
def next_greater(number):
    
    n = len(number)
    i = n-1
    
    while i > 0:                                # if number is inc from right to left, keep moving else break
        if int(number[i-1] < number[i]):
            break
        i -= 1
        
    if i == 0:                                  # if i = 0, number is dec, so no possible
        return '-1'

    j = n-1                                     # val at i = 7 so find number greater than i-1 i.e 1
    while j >= i:                                
        if number[j] > number[i-1]:
            break
        j -= 1
                                                      # here val at j is 2
    number[j], number[i-1] = number[i-1], number[j]   # swap that number, because this number is just greater (swap 2 and 1)
    
    x = i                                        # 27421
    y = n-1                                      # since right array is already decreasing, so swapped number must be in a dec place (here at last)
    while x <= y:                                # so just reverse this second array to make it sorted increasing (21247)
        number[x], number[y] = number[y], number[x]
        x += 1
        y -= 1
    return number
    
if __name__ == '__main__':
    t = int(input())
    while t:
        number = input()
        ans = next_greater(list(number))
        if ans == '-1':
            print('not possible')
        else:
            #print(ans)
            print(''.join(ans))
        t -= 1