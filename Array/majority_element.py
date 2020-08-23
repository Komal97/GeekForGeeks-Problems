'''
https://practice.geeksforgeeks.org/problems/majority-element/0
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1
Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
'''

# Moore Voting Algorithm
# overall idea is - take 1 majority element as compare other elements, which do not match they cancel out each 
# other's count
def find_candidate(arr, n):
    
    count = 1                               # take first element as majority element(maintain index)
    maj_index = 0
    
    for i in range(1, n):
        if arr[maj_index] == arr[i]:        # if maj_index and curr same, then count ++
            count += 1
        else:
            count -= 1                      # else count--

        if count == 0:                      # if count become 0 then take current element as majority element 
            count = 1
            maj_index = i
            
    return arr[maj_index]           

def is_majority(el, arr, n):
    
    count = 0
    for i in range(n):
        if arr[i] == el:
            count += 1
    
    return n//2 < count 

def majority_element(arr, n):
    
    candidate = find_candidate(arr, n)                              # find candidate using algo
    return candidate if is_majority(candidate, arr, n) else -1      # check candidate frequency
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        print(majority_element(arr, n))
        t -= 1