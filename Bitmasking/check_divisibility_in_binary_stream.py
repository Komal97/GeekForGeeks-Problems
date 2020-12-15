'''
https://www.geeksforgeeks.org/check-divisibility-binary-stream/
Stream of binary number is coming, the task is to tell the number formed so far is divisible by a given number n.
At any given time, you will get 0 or 1 and tell whether the number formed with these bits is divisible by n or not.
'''

# method - 1
# num can cause integer overflow
n = int(input())
num = 0
while True:

    incoming_bit = int(input())
    if incoming_bit == 1:
        num = num*2 + 1
    elif incoming_bit == 0:
        num = num*2
    else:
        break
    
    print((num % n) == 0)
    

# method - 2
# solving integer overflow problem by keep remainder only
n = int(input())
remainder = 0
while True:

    incoming_bit = int(input())
    if incoming_bit == 1:
        remainder = (remainder*2 + 1)%n
    elif incoming_bit == 0:
        remainder = (remainder*2)%n
    else:
        break
    
    print((remainder % n) == 0)