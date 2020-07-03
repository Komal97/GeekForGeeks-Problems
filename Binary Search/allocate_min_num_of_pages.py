'''
https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages/0
You are given N number of books. Every ith book has Pi number of pages. 
You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations, and print this minimum value. 
Each book will be allocated to exactly one student. Each student has to be allocated atleast one book.
Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding).
Input:
2
4
12 34 67 90
2
3
15 17 20
2
Output:
113
32

Explaination:
Testcase 1:Allocation can be done in following ways:
{12} and {34, 67, 90}     Maximum Pages = 191
{12, 34} and {67, 90}     Maximum Pages = 157
{12, 34, 67} and {90}        Maximum Pages = 113

Therefore, the minimum of these cases is 113, which is selected as output.

Testcase 2: Allocation can be done in following ways:
{15} and {17, 20} Maximum pages = 37
{15, 17} and {20} Maximum Pages = 32

So, the output will be 32.
'''

def isValid(arr, n, no_of_students, max_pages):
    
    student = 1
    total_pages = 0
    
    for num in arr:
        total_pages += num
        if total_pages > max_pages:
            student += 1
            total_pages = num
        if student > no_of_students:
            return False
    return True
    
def allocate(arr, n, no_of_students):
    
    if n < no_of_students:
        return -1
        
    start = 0
    end = 0
    for num in arr:
        end += num
        start = max(start, num)
    
    ans = -1
    while start <= end:
        mid = start + (end-start)//2
        if isValid(arr, n, no_of_students, mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1
    print(ans)

if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        no_of_students = int(input())
        allocate(arr, n, no_of_students)
        t -= 1