'''
https://practice.geeksforgeeks.org/problems/faulty-wiring-and-bulbs/0
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. 
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. "0 represents the bulb is off and 1 represents the bulb is on."
Input:
2
4
0 0 0 0
4
1 0 0 1
Output:
1
2
'''

# method - 1 => current 1 change due to toggle of prv 0 and again toggle 1 itself
def wires_and_bulbs(arr, n):
    
    count = 0
    i = 0
    while i < n:
        zeroes = 0
        ones = 0
        while i<n and arr[i] == 0:
            zeroes += 1
            i += 1
            
        while i<n and arr[i] == 1:
            ones += 1
            i += 1
        if zeroes > 0 or ones > 0:
            if zeroes > 0:                              # toggle 0
                count += 1
                if ones > 0:                            # 1 is toggled only if there is 0 before
                    count += 1
            i -= 1
        i += 1
    print(count)
    
# method - 2 => maintain current states of 1 and 0 as flag, if at any point flag is out of order, means it is flipped
def wires_and_bulbs(arr, n):
    
    count = 0
    
    if arr[0] == 1:                         # take 1 as true and since not needed to flip, so count as 0
        flag = True
    else:                                   # take 0 as false and since it is needed to flip, so count as 1
        flag = False
        count = 1
    
    # if 0 and flag is out of order, means it is flipped before, so again flip it 
    for i in range(1, n):
        if arr[i] == 0 and flag == True:    
            count += 1
            flag = False
        elif arr[i] == 1 and flag == False:
            count += 1
            flag = True
        
    print(count)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        wires_and_bulbs(arr, n)
        t -= 1