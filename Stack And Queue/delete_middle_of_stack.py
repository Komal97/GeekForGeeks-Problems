'''
https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1
Given a stack with push(), pop(), empty() operations, delete the middle of it without using any additional data structure.
Middle: ceil(size_of_stack/2.0)
Input:
3
5
1 2 3 4 5
7
1 2 3 4 5 6 7
4
1 2 3 4
Output:
5 4 2 1
7 6 5 3 2 1
4 3 1
'''

# recusrsively remove elements
def deleteMid(s, sizeOfStack, current):
    mid = (sizeOfStack+1)//2
    def delete(s, mid, current):
        if len(s) > 0 and current == mid:
            s.pop()
            return
        
        x = s.pop()
        delete(s, mid, current+1)
        s.append(x)
        
    delete(s, mid, current+(sizeOfStack%2))
    return s
