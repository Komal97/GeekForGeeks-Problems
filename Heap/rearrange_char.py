'''
https://practice.geeksforgeeks.org/problems/rearrange-characters/0

https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
Given a string S with repeated characters (only lowercase). The task is to rearrange characters in a string such that no two adjacent characters are same.
Input:
3
geeksforgeeks
bbbabaaacd
bbbbb

Output:
1
1
0
'''
# use PnC concept, find maxfreq and check n/2 >= maxfreq, maxfreq should be n/2 max so that other elements can be placed at alternate places
def rearrangeChar(string):
    h = {}
    maxfreq = -1
    for ch in string:
        if ch not in h:
            h[ch] = 1
        else:
            h[ch] += 1
        maxfreq = max(maxfreq, h[ch])
    
    return (len(string)+1)//2 >= maxfreq

# to rearrange characters
def rearrangeChar(string):
    
    # create frequency map
    h = {}
    for ch in string:
        if ch not in h:
            h[ch] = 1
        else:
            h[ch] += 1
    
    # build maxheap (freq, char)
    heap = []
    for ch in h:
        heappush(heap, [-h[ch], ch])
    
    ans = ''
    prev = [0, '#']

    # take char with max freq, add in ans and temporarily pop and save in prev variable
    # while popping next character, push prev if its freq > 0
    while len(heap) > 0:
        
        # pop current
        top = heap[0]
        heappop(heap)
        
        # add current char in ans
        ans += top[1]
        
        # push previous character
        if -prev[0] > 0:
            heappush(heap, [prev[0], prev[1]])
        
        # assign current as previous
        top[0] = -(abs(top[0]) - 1)
        prev = top
    
    # in end, either no or 1 character with some freq is left
    # if no character then length become equal
    # if 1 character left with freq then their length won't be equal
    return len(string) == len(ans)

if __name__ == '__main__':
    
    t = int(input())
    while t:
        string = input()
        print(int(rearrangeChar(string)))
        t -= 1
        
        