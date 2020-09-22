'''
https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1
Given a binary matrix your task is to find all unique rows of the given matrix.
Example 1:
Input:
row = 3, col = 4
M[][] = {{1 1 0 1},{1 0 0 1},{1 1 0 1}}
Output: 1 1 0 1 $1 0 0 1 $
Explanation: Above the matrix of size 3x4 looks like
1 1 0 1
1 0 0 1
1 1 0 1
The two unique rows are 1 1 0 1 and 1 0 0 1 .
'''

# insert matrix in trie
# if that row is already present in trie, don't append it in ans
class Node:
    def __init__(self, data):
        self.data = data
        self.h = {}
        self.terminal = False
        
class Trie:
    def __init__(self):
        self.__root = Node('')
        
    def insert(self, row):
        temp = self.__root
        for num in row:
            if num not in temp.h:
                child = Node(num)
                temp.h[num] = child
                temp = child
            else:
                temp = temp.h[num]
        
        if temp.terminal == True:
            return False
        else:
            temp.terminal = True
            return True

def creatematrix(row, col, matrix):
    
    a = 0
    mat = []
    for i in range(row):
        r = []
        for j in range(col):
            r.append(matrix[a])
            a += 1
        mat.append(r)
    return mat
        
def uniqueRow(row, col, matrix):
    
    mat = creatematrix(row, col, matrix)
    ans = []
    t = Trie()
    for i in range(row):
        flag = t.insert(mat[i])
        if flag:
            ans.append(mat[i])
    
    return ans
