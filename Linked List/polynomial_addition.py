'''
https://practice.geeksforgeeks.org/problems/polynomial-addition/1
Given two polynomial numbers represented by a linked list. The task is to complete the  function addPolynomial() 
that adds these lists meaning adds the coefficients who have same variable powers.
Input:
2
1
1 2
1
1 3
2
1 3 2 2
2
3 3 4 2
Output:
1x^3 + 1x^2
4x^3 + 6x^2

Explanation:
Testcase 1: Since, x2 and x3 both have different powers as 2 and 3. So, their coefficient can't be added up.
Testcase 2: Since, x3 has two different coefficients as 3 and 1. Adding them up will lead to 4x3. Also, x2 has two coefficients as 4 and 2. 
So, adding them up will give 6x2.
'''
# if power of both are equal, then add else move pointer with less power 
def addPolynomial(poly1, poly2):
    '''
	class node:
		def __init__(self, coeff, pwr):
			self.coef = coeff
			self.next = None
			self.power = pwr
	'''
    head = None
    tail = None
    
    while poly1 and poly2:
        coef = 0
        power = 0
        if poly1.power > poly2.power:
            coef = poly1.coef
            power = poly1.power
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            coef = poly2.coef
            power = poly2.power
            poly2 = poly2.next
        else:
            coef = poly1.coef + poly2.coef
            power = poly1.power
            poly1 = poly1.next
            poly2 = poly2.next
        n = node(coef, power)
        if not head:
            head = n
            tail = head
        else:
            tail.next = n
            tail = tail.next
    
    if poly1:
        tail.next = poly1
    if poly2:
        tail.next = poly2
        
    return head