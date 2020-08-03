'''
https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0
Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. 
Match nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. 
It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
Output:
For each test case, output the matched array of nuts and bolts in separate lines, where each element in the array is separated by a space. Print the elements in the following order ! # $ % & * @ ^ ~ 
Input:
2
5
@ % $ # ^
% @ # $ ^
9
^ & % @ # * $ ~ !
~ # @ % & * $ ^ ! 

Output:
# $ % @ ^
# $ % @ ^
! # $ % & * @ ^ ~
! # $ % & * @ ^ ~
'''

def nuts_and_bolts(arr1, arr2, n):
    h = {'!': 0, '#': 0, '$': 0, '%': 0, '&': 0, '*': 0, '@': 0, '^': 0, '~': 0}
    arr = ['!', '#', '$', '%', '&', '*', '@', '^', '~']
    
    for ch in arr1:
        h[ch] += 1
    
    for ch in arr2:
        h[ch] += 1
    
    for ch in arr:
        if h[ch] == 2:
            print(ch, end = ' ')
    print()
    for ch in arr:
        if h[ch] == 2:
            print(ch, end = ' ')
    print()

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr1 = input().split()
        arr2 = input().split()
        nuts_and_bolts(arr1, arr2, n)
        t -= 1