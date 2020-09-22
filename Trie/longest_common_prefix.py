'''
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

# insert strings in trie
# append characters in ans will len(map) == 1 and node.terminal == False
class Solution:
    class Trie:
        class TrieNode:
            def __init__(self, data):
                self.data = data
                self.h = {}
                self.terminal = False
            
        def __init__(self):
            self.__root = self.TrieNode('')
        
        def getTrieNode(self):
            return self.__root
        
        def insert(self, word):
            cur_node = self.getTrieNode()
            
            for ch in word:
                if ch not in cur_node.h:
                    cur_node.h[ch] = self.TrieNode(ch)    
                cur_node = cur_node.h[ch]
                
            cur_node.terminal = True        
        
    def longestCommonPrefix(self, strs: List[str]):
        
        t = self.Trie()
        n = len(strs)
        
        if n == 0:
            return ''
        elif n == 1:
            return strs[0]
        for s in strs:
            t.insert(s)
        
        cur_node = t.getTrieNode()
        
        prefix = ''
        while len(cur_node.h) == 1 and cur_node.terminal == False:
            key = list(cur_node.h.keys())[0]
            prefix += key
            cur_node = cur_node.h[key]

        return prefix