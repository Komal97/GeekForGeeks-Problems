'''
https://practice.geeksforgeeks.org/problems/subsets/0
Given an array of integers that might contain duplicates, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Input:
2
3
1 2 2
4
1 2 3 3
Output:
()(1)(1 2)(1 2 2)(2)(2 2)
()(1)(1 2)(1 2 3)(1 2 3 3)(1 3)(1 3 3)(2)(2 3)(2 3 3)(3)(3 3)
'''

# either include or exclude an element in output 
def printSubsets(arr, i, n, output, ans):
    
    if i == n:
        ans.add(output)
        return
    
    printSubsets(arr[1:], i+1, n, output + ' ' +str(arr[0]), ans)
    printSubsets(arr[1:], i+1, n, output, ans)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        
        ans = set()
        printSubsets(arr, 0, n, '', ans)
 
        for a in sorted(ans):
            print('(' + a.strip() + ')', end = '')
        print()
        t -= 1
        
'''
https://www.interviewbit.com/problems/subset/
Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :
If S = [1,2,3], a solution is:
[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
'''

class Solution:
    
    # method - 1
    def subsets(self, A):
        n, ans, _ = len(A), [], A.sort()
        
        def generate(i, soln):
            if i == n:
                ans.append(soln)
                return
            
            generate(i + 1, soln)
            generate(i + 1, soln + [A[i]])
   
        generate(0, [])
        ans.sort()
        return ans
    
    # method - 2
	def subsets(self, A):
	    
	    n, res, _ = len(A), [], A.sort(reverse=True)
	    
	    for i in range(n):
	        x = [A[i]]
	        res.extend([x + y for y in res])
	        res.append(x)
	   
	    res.append([])
	    res.reverse()
	    return res

'''
https://www.interviewbit.com/problems/subsets-ii/
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
'''

class Solution:
    
    # method - 1
    def subsetsWithDup(self, A):
        
        n, ans, _ = len(A), set(), A.sort()
        
        def generate(i, soln):
            if i == n:
                ans.add(tuple(soln))
                return
            
            generate(i + 1, soln)
            generate(i + 1, soln + [A[i]])
   
        generate(0, [])
        ans = list(ans)
        ans.sort()
        return ans
        