'''
https://practice.geeksforgeeks.org/problems/count-possible-ways-to-construct-buildings/0
Given N, the number of plots on either sides of the road. Find the total ways to construct buildings in the plots such that there is a space between any 2 buildings. 
All plots on one side of the road are continuous. Lets suppose ‘*’ represents a plot, then for N=3, the plots can be represented as * * * | | * * *                               
Where || represents the road.        
Input:
1
3
Output:
25

Explanation:
3 plots, which means possible ways for one side are BSS, BSB, SSS, SBS, SSB where B represents a building and S represents an empty space
Total possible ways are 25, because a way to place on one side can correspond to any of 5 ways on other side.
'''

# recursive
M = 1000000007
def countWays(n, out):
    if n == 0:
        return 1
    
    val = 0
    if out == '' or out[-1] == 'S':
        val += countWays(n-1, out+'S')
        val += countWays(n-1, out+'B')
    elif out[-1] == 'B':
        val += countWays(n-1, out+'S')
        
    return (val)%M

# iterative
def countWays(n):
    if n == 0:
        return 0
    
    old_space = 1
    old_build = 1
    for i in range(2, n+1):
        new_space = (old_space + old_build)%M       # space and building after space
        new_build = old_space                       # only space after building
        old_space = new_space
        old_build = new_build
        
    return old_space + old_build

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ans = countWays(n, '')
        print((ans*ans)%M)
        t -= 1