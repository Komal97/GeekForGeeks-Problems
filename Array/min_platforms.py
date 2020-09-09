'''
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.
Input:
2
6 
0900  0940 0950  1100 1500 1800
0910 1200 1120 1130 1900 2000
3
0900 1100 1235
1000 1200 1240 

Output:
3
1
'''

# sort arrival and departure
# maximum overlapping at a time is maximum number of platforms required
# if train arrived before previous departure, then platform++
# if train departed, platform -= 1
def find_min_platforms(arrival, depart, n):
      
    arrival.sort()
    depart.sort()M
    
    maxplatforms = 1
    platforms = 1
    
    i = 1
    j = 0
    while i < n and j < n:
        if arrival[i] <= depart[j]:
            platforms += 1
            maxplatforms = max(maxplatforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    print(maxplatforms)
    
t = int(input())
while t:
    n = int(input())
    arrival = list(map(int, input().split()))
    depart = list(map(int, input().split()))
    find_min_platforms(arrival, depart, n)
    t -= 1