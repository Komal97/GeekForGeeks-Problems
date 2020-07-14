'''
https://practice.geeksforgeeks.org/problems/sum-tree/1
Write a function that returns true if the given Binary Tree of size N is SumTree else return false. A SumTree is a Binary Tree in which value of each node x is equal to sum of nodes present in its left subtree and right subtree . 
Input:
2
3 1 2
10 20 30 10 10

Output:
1
0
'''

# create a custom pair class with sum calculated and subtree is sum tree or not
# check left tree is sumtree, right tree is sumtree and root data = left subtree + right subtree
class Pair:
    def __init__(self):
        self.summ = 0
        self.isSum = True
        
def checkSumTree(root):
    if root == None:
        p = Pair()
        return p
  
    lpair = checkSumTree(root.left)
    rpair = checkSumTree(root.right)
    
    cur_pair = Pair()
    cur_pair.summ = root.data
    if root.left != None or root.right != None:
        val = lpair.summ + rpair.summ 
        cur_pair.isSum = lpair.isSum and rpair.isSum and (val==root.data)
        cur_pair.summ = root.data + val

    return cur_pair

def isSumTree(root):
    
    pair = checkSumTree(root)
    return pair.isSum