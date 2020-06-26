'''
https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.
Input:
1
4
4 6 6 5 7 3 4 5
Output:
1

Explanation:
Testcase 1: there are 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where truck can make a circular tour is 2nd petrol pump. Output in this case is 1 (index of 2nd petrol pump).
'''



def tour(lis, n):
    '''
    lis[][0]:Petrol
    lis[][1]:Distance
    '''
    
    # uses concept of queue 
    start = 0
    end = 1
    cur = lis[0][0] - lis[0][1]
    if n == 1:
        return -1 if cur<0 else 0
    
    # loop until a round is complete
    while start!= end or cur<0:  
        # HERE WE ENQUEUE   
        # while completing round, we check if cur is less than 0 means starting point we were considering was wrong   
        # so we move our start pointer to end because before that all makes cur negative                                  
        while start!=end and cur<0:
            # HERE WE START DEQUEUE
            cur -= lis[start][0] - lis[start][1]
            start = (start+1)%n
            # if at any point start becomes 0 means we come to 0 again, means no route found
            if start == 0:
                return -1
        # if cur is poisitive means we can move forward and start incrementing 'end' pointer
        cur += lis[end][0] - lis[end][1]
        end = (end+1)%n
        
    return start