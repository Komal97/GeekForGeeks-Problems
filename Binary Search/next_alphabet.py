'''
find index of next alphabet from string
Input: abfh
       key = f
Ouput: 3
'''

# same as that of ceil problem
# change is we have to find next element always even if key is present in string                        
def next_alphabet(string, x):
    
    s = 0
    e = len(string)-1
    ans = -1
    
    while s<=e:
        mid = s + (e-s)//2
        if string[mid] <= x:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1
    return ans 

if __name__ == '__main__':
   
    string = input()
    x = input()
    print(next_alphabet(string, x))
      