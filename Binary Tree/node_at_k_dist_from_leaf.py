'''
https://practice.geeksforgeeks.org/problems/node-at-distance/1
Given a Binary Tree and a positive integer k. The task is to count all distinct nodes that are distance k from a leaf node. A node is at k distance from a leaf if it is present k levels above the leaf and also, is a direct ancestor of this leaf node. If k is more than the height of Binary Tree, then nothing should be counted.
Input:
2
1 2 3 4 5 6 7 N N N N N 8
2
1 3 N 5 N 7 8 N N 9
4
Output:
2
1

Explanation:
Testcase 1:
There are only two unique nodes that are at a distance of 2 units from the leaf node. 
(node 3 for leaf with value 8 and node 1 for leaves with values 4, 5 and 7)
Note that node 2 isn't considered for leaf with value 8 because it isn't a direct ancestor of node 8
'''

# use recursion to store node to leaf path and on encountering leaf node, put len(arr)-k element in set
def printKDistantfromLeaf(root, k):
    
    ans = set()
    output = []
    def uniqueNum(root, k):
        nonlocal ans
        nonlocal output
        
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            if len(output) >= k:
                ans.add(output[len(output)-k])
            return
        
        output.append(root)
        uniqueNum(root.left, k)
        uniqueNum(root.right, k)
        output.pop()                # list is pass by reference so need to pop out values
        
    uniqueNum(root, k)    
    return len(ans)