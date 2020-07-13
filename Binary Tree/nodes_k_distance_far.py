'''
https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1
Given a binary tree, a target node in the binary tree, and an integer value k, find all the nodes that are at distance k from the given target node. No parent pointers are available.
Input:
2
20 8 22 4 12 N N N N 10 14
8
2
20 7 24 4 3 N N N N 1
7
2

Output:
10 14 22 
1 24
'''

class solver:
        
    # find node to path
    def findPath(self, root, target, path):
        if root == None:
            return False
        
        # if data become equal to target
        if root.data == target:
            path.append(root)
            return True
        
        # while returning, we move towards root so append node
        left = self.findPath(root.left, target, path)
        if left:
            path.append(root)
            return True
        
        right = self.findPath(root.right, target, path)
        if right:
            path.append(root)
            return True
        
        # if node not found
        return False
    
    # print k level down from the given node
    def printLevel(self, root, k, blocker, ans):
        if root == None or k < 0 or root == blocker:
            return
        
        if k == 0:
            ans.append(root.data)
            return
        self.printLevel(root.left, k-1, blocker, ans)
        self.printLevel(root.right, k-1, blocker, ans)
        
    # print all nodes which are k distance away from given node
    def KDistanceNodes(self,root,target,k):
        
        ans = []
        path = []
        check = self.findPath(root, target, path)
        if not check:
            return ans
  
        for i in range(len(path)):
            blocker = path[i-1] if i!=0 else None
            self.printLevel(path[i], k-i, blocker, ans)
        ans.sort()
        return ans
