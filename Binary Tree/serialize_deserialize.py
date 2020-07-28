'''
https://practice.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1
Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to tree and returns it.
Example:
Input:
2
1 2 3
10 20 30 40 60
Output:
2 1 3
40 20 60 10 30

Explanation:
Testcase 2: Given tree is 
                         10
                       /   \
                     20     30
                   /   \
                 40    60
Hence, the given output is 40 20 60 10 30.
'''

# using preorder, store data in array and Null as -1(marker)
def serialize(root, A):
    
    if root == None:
        A.append(-1)
        return
    
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)
    
# using preorder, build tree with -1 as None
def buildtree(A, i):
    if A[i[0]] == -1:
        i[0] += 1
        return None
    
    n = Node(A[i[0]])
    i[0] += 1
    n.left = buildtree(A, i)
    n.right = buildtree(A, i)
    return n
    
def deSerialize(A):
    i = [0]
    return buildtree(A, i)