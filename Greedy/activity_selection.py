'''
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room?
Input:
2
6
1 3 0 5 8 5
2 4 6 7 9 9
8
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252  

Output:
1 2 4 5
6 7 1
'''

# since we need to find max rooms, means meeting should end early
# sort by finish time, check finish <= start, then count++ and update finish
def find_max_meeting(start, finish, n):
    
    pair = []
    for i in range(n):
        pair.append([start[i], finish[i], i+1])
    
    pair.sort(key = lambda x: x[1])

    fin = pair[0][1]
    ind = pair[0][2]
    for s, e, i in pair:
        if s >= fin:
            print(ind, end = ' ')
            fin = e
            ind = i
            
    print(ind)

t = int(input())
while t:
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    find_max_meeting(start, finish, n)
    t -= 1