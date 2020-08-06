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

# method - 1 => initialize map with given characters as key and value as freq
# for maintaining order, keep arr with characters initialized in order
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

# method - 2 -> using quick sort (because only algo which can pick element)
# for partition nuts, take end from bolts as pivot
# then partition bolt using pivot of nuts
def partition(arr, s, e, pivot):
    
    i = s-1
    j = s

    while j<e:
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        elif arr[j] == pivot:
            arr[j], arr[e] = arr[e], arr[j]
            j -= 1
        j += 1
    i += 1
    arr[i], arr[e] = arr[e], arr[i]
    return i

def quicksort(nuts, bolts, s, e):

    if s>=e:
        return
    
    p = partition(nuts, s, e, bolts[e])
    partition(bolts, s, e, nuts[p])
    quicksort(nuts, bolts, s, p-1)
    quicksort(nuts, bolts, p+1, e)

def nuts_and_bolts(nuts, bolts, n):
    quicksort(nuts, bolts, 0, n-1)
    print(*nuts, sep = ' ')
    print(*bolts, sep = ' ')
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        nuts = input().split()
        bolts = input().split()
        nuts_and_bolts(nuts, bolts, n)
        t -= 1