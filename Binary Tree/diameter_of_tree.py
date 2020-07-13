'''
https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
Given a Binary Tree, find diameter of it.
Input:
2
1 2 3
10 20 30 40 60 

Output:
3
4

Explanation:
Testcase1: The tree is
        1
     /     \
   2        3
The diameter is of 3 length.
Testcase2: The tree is
                            10
                        /       \
                     20         30
                  /       \
               40       60
The diameter is of 4 length.
'''
# Method 1 - O(n^2) - O(n) for finding diameter at each node and O(n) for finding height
# find diameter of tree including root node - left height + right height + 1
# find diameter from left 
# find diameter from right 
# find max of all 3 cases
def height(root):
    if root == None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)
    return max(rh, lh)+1
    
def diameter(root):
    if root == None:
        return 0
    
    h = height(root.left) + height(root.right) + 1
    d1 = diameter(root.left)
    d2 = diameter(root.right)
    
    return max(h, max(d1, d2))

# method - 2 - O(n)
# Find diameter and height at each node
# and we save height at each node in a pair
class Pair:
    def __init__(self):
        self.height = 0
        self.diameter = 0
        
def diameter(root):
    
    def findDiamater(root):
        if root == None:
            end_node_pair = Pair()
            end_node_pair.diameter = 0
            end_node_pair.height = 0
            return end_node_pair
            
        d1_pair = findDiamater(root.left)
        d2_pair = findDiamater(root.right)
        
        # saving height from current node
        curr_node_pair = Pair()
        curr_node_pair.height = max(d1_pair.height, d2_pair.height) + 1
        
        # find diameter based on 3 conditions
        height = d1_pair.height + d2_pair.height + 1
        curr_node_pair.diameter = max(height, max(d1_pair.diameter, d2_pair.diameter))
        return curr_node_pair

    return findDiamater(root).diameter