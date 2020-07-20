'''
https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1
Given a BST and an integer. Find the least absolute difference between any node value of the BST and the given integer.
Input:
2
10 2 11 1 5 N N N N 3 6 N 4
13
8 1 9 N 4 N 10 3
9

Output:
2
0

Explanation:

Testcase1:
K=13. The node that has value nearest to K is 11. so the answer is 2
Testcase2:
K=9. The node that has value nearest to K is 9. so the answer is 0.
'''

# keep ans containing min difference, if root.data > K then move left(because smallest diff will always be in left) else move right
def minDiff(root, K):
    
    def findDiff(root, K):
        
        nonlocal ans
        if root == None or ans == 0:
            return
       
        ans = min(ans, abs(K-root.data))
        if root.data > K:
            findDiff(root.left, K)
        elif root.data < K:
            findDiff(root.right, K)
            
    ans = float('inf')
    findDiff(root, K)
    return ans