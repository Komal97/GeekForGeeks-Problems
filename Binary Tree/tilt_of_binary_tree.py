'''
https://practice.geeksforgeeks.org/problems/tilt-of-binary-tree/1
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null nodes are assigned tilt to be zero. Therefore, tilt of the whole tree is defined as the sum of all nodes’ tilt.
Input :
    4
   / \
  2   9
 / \   \
3   5   7
Output : 15
Explanation: 
Tilt of node 3 : 0
Tilt of node 5 : 0
Tilt of node 7 : 0
Tilt of node 2 : |3-5| = 2
Tilt of node 9 : |0-7| = 7
Tilt of node 4 : |(3+5+2)-(9+7)| = 6
Tilt of binary tree : 0 + 0 + 0 + 2 + 7 + 6 = 15
Input:
2
2
1 2 L 1 3 R
5
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L
Output:
1
110
'''

# method - 1
# use postorder traversal
# create a custom pair of summ(sum of subtree) and diff(sum of diff of subtree)
class Pair:
    def __init__(self):
        self.summ = 0
        self.diff = 0
        
def findTilt(root):
    
    pair = Pair()
    if root == None:
        return pair
        
    lpair = findTilt(root.left)
    rpair = findTilt(root.right)
    
    pair.diff = abs(lpair.summ - rpair.summ) + lpair.diff + rpair.diff
    pair.summ = lpair.summ + rpair.summ + root.data
    return pair
    
def tiltTree(root):
    
    if root == None:
        return 0
    return findTilt(root).diff

# method - 2
# calculate and return summ in recursion and maintain a static tilt variable
# tilt is updated before returning sum in postorder
def findTilt(root, tilt):
    
    if root == None:
        return 0
        
    lsum = findTilt(root.left, tilt)
    rsum = findTilt(root.right, tilt)
    
    tilt[0] += abs(lsum - rsum)
    return lsum + rsum + root.data
    
def tiltTree(root):
    
    if root == None:
        return 0
    tilt = [0]
    summ = findTilt(root, tilt)
    return tilt[0]