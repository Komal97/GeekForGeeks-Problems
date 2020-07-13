'''
https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1
Given a Binary Tree, print the vertical traversal of it starting from the leftmost level to the rightmost level.
Input:
3
2 N 3 4 N
1 2 3 4 5 N 6
3 1 5 N 2 4 7 N N N N 6 
Output:
2 4 3
4 2 1 5 3 6
1 3 2 4 5 6 7
Explanation:
Testcase1:
         2
           \
            3
           /
         4
As it is evident from the above diagram that during vertical traversal 2, 4 will come first, then 3. So output is 2 1 5 3
Testcase2:
             1
           /   \
         2       3
      /     \     \
    4       5      6
As it is evident from the above diagram that during vertical traversal 4 will come first, then 2, then 1,5, then 3 and then 6. So the output is 4 2 1 5 3 6.
'''

# same as level order
# take root as 0(k), move left -> k-1 and move right -> k+1
from collections import deque
def verticalOrder(root): 
    
    if root == None:
        return
    
    q = deque()
    q.append((root, 0))
    
    h = {}
    
    while len(q)>0:
        size = len(q)
        
        for i in range(size):
            node, k = q.popleft()
            if k not in h:
                h[k] = []
            h[k].append(node.data)
                
            if node.left:
                q.append((node.left,k-1))
            if node.right:
                q.append((node.right,k+1))

    h = sorted(h.items(), key = lambda x: x[0])
    
    ans = []
    for dist, nodelist in h:
        ans.extend(nodelist)
    return ans