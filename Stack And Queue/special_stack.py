'''
https://practice.geeksforgeeks.org/problems/special-stack/1
https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() 
which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.
Expected Time Complexity: O(1) for all the 5 functions.
Expected Auxiliary Space: O(1) for all the 5 functions.
Input:
1
5
18 19 29 15 16
Output:
15
'''
# method - 1, create auxilliary stack with minimum element till now and always return top of stack
# O(1) time & O(n) space
min_stack = []
def push(arr, ele):
    global min_stack
    arr.append(ele)
    if len(min_stack) == 0 or min_stack[-1] >= ele:
        min_stack.append(ele)
    
def pop(arr):
    if isEmpty(arr):
        return
    global min_stack
    x = arr.pop()
    if min_stack[-1] == x:
        min_stack.pop()

def isFull(n, arr):
    return len(arr) == n

def isEmpty(arr):
    return len(arr) == 0

def getMin(n, arr):
    global min_stack
    x = min_stack[-1] if len(min_stack) != 0 else -1
    min_stack = []
    return x

# method - 2, O(1) time & O(1) space
# while pushing, push 2 * coming min element - prev min element = new stack top
# while popping, pop 2 * going min element - stack top = prev min element
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=float('inf')

    def push(self,x):
        # if stack is empty, push first element and set it as min elemnet also
        if len(self.s) == 0:
            self.s.append(x)
            self.minEle = x
        # if x > min element so directly push
        elif x > self.minEle:
            self.s.append(x)
        # if x <= min element, push element and change min element 
        else:
            y = x + x - self.minEle
            self.s.append(y)
            self.minEle = x

    def pop(self):
        # if stack is empty means no element to pop, return -1
        if len(self.s) == 0:
            return -1
        # if stack top is greater than min element, so directly pop
        if self.s[-1] > self.minEle:
            return self.s.pop()
        else:
            x = self.minEle
            y = self.s.pop()
            # after popping stack become empty, so change min element too
            if len(self.s) == 0:
                self.minEle = float('inf')
            else:
                self.minEle = 2*self.minEle - y
            return x

    def getMin(self):
        return self.minEle if self.minEle else -1