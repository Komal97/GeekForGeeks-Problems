'''
https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.
Input:
2
3 2 1
7 7 9 8 8 6 N 10 9
Output:
3 1 2
7 9 7 8 8 6 9 10

Explanation:
Testcase 1: Given tree is
                         3
                      /    \
                    2        1
Hence the zigzag traversal will be 3 1 2.
'''

# for odd level, push children left to right and for even, push right to left in child stack
# if main stack become empty, means a level is complete, then make main stack = child stack and make child stack empty & level++
def zigZagTraversal(root):
    
    ans = []
    main_stack = []
    child_stack = []
    level = 1
    
    main_stack.append(root)
    
    while len(main_stack) > 0:
        node = main_stack.pop()
        ans.append(node.data)
        # level is odd
        if level&1:
            if node.left:
                child_stack.append(node.left)
            if node.right:
                child_stack.append(node.right)
        else:
            if node.right:
                child_stack.append(node.right)
            if node.left:
                child_stack.append(node.left)
        if len(main_stack) == 0:
            main_stack = child_stack
            child_stack = []
            level += 1
    return ans