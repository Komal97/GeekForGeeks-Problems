'''
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 
Example 1:
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output: 240.00
Explanation: Total maximum value of item we can have is 240.00 from the given capacity of sack. 

Example 2:
Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output: 160.00
Explanation: Total maximum value of item we can have is 160.00 from the given capacity of sack.
'''

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    
    # sort object in reverse order on basis of 1 kg value which is value/weight
    setattr(Item, '__lt__', lambda self, other: (self.value/self.weight) < (other.value/other.weight))
    Items.sort(reverse=True)
    
    cost = 0
    for item in Items:
        # if item weight is considerable then add its cost
        if item.weight <= W:
            cost += item.value
            W -= item.weight
        # else add fraction of item
        else:
            new_cost = (W/item.weight)*item.value
            cost += new_cost
            break
        
    return round(cost, 2)

