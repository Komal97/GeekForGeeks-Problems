'''
https://practice.geeksforgeeks.org/problems/finding-position/0
Some people are standing in a queue. A selection process follows a rule where people standing on even positions are selected. 
Of the selected people a queue is formed and again out of these only people on even position are selected. 
This continues until we are left with one person. Find out the position of that person in the original queue.
Input:
2
5
9
Output:
4
8
'''

# maximum power of 2 is the left person
def find_pos(n):
    
    c = -1
    while n:
        n >>= 1
        c += 1
    print(2**c)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        find_pos(n)
        t -= 1