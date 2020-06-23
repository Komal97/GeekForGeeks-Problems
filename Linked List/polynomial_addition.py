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
    polysum_h = None
    polysum_t = None
    while(poly1 != None and poly2 != None):
        if poly1.power == poly2.power:
            if polysum_h == None:
                polysum_h = node(poly1.coef + poly2.coef, poly2.power)
                polysum_t = polysum_h
            else:
                n = node(poly1.coef + poly2.coef, poly2.power)
                polysum_t.next = n
                polysum_t = polysum_t.next
            poly1 = poly1.next
            poly2 = poly2.next
        elif poly1.power < poly2.power:
            if polysum_h == None:
                polysum_h = node(poly2.coef, poly2.power)
                polysum_t = polysum_h
            else:
                n = node(poly2.coef, poly2.power)
                polysum_t.next = n
                polysum_t = polysum_t.next
            poly2 = poly2.next
        else:
            if polysum_h == None:
                polysum_h = node(poly1.coef, poly1.power)
                polysum_t = polysum_h
            else:
                n = node(poly1.coef, poly1.power)
                polysum_t.next = n
                polysum_t = polysum_t.next
            poly1 = poly1.next
    if poly1:
        polysum_t.next = poly1
    if poly2:
        polysum_t.next = poly2
    return polysum_h