'''
https://www.geeksforgeeks.org/reduce-a-number-to-1-by-performing-given-operations/
Given a number N. The task is to reduce the given number N to 1 in the minimum number of steps. You can perform any one of the below operations in each step.
Operation 1: If the number is even then you can divide the number by 2.
Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).
You need to print the minimum number of steps.
Input : n = 15
Output : 5
 15 is odd 15+1=16    
 16 is even 16/2=8     
 8  is even 8/2=4 
 4  is even 4/2=2     
 2  is even 2/2=1     

Input : n = 7
Output : 4
    7->6    
    6->3 
    3->2    
    2->1  
'''

# if n is even then n/2
# if n is odd - 2 cases => if n%4==1(n = 4x+1) then n = n-1, if n%4==3 (n = 4x+1) then n = n+1
def min_moves(n):
    if n == 3:                  # spl case - it is of 4x+3 type but we do n= n-1
        return 2
    
    count = 0
    while n != 1:
        if n%2 == 0:
            n = n//2
        elif n%4 == 1:
            n = n-1
        elif n%4 == 3:
            n = n+1
        count += 1
    return count


n = int(input())
ans = min_moves(n)
print(ans)