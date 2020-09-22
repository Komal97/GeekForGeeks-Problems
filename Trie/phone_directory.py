'''
https://practice.geeksforgeeks.org/problems/phone-directory/0
Given a list of contacts which exist in a phone directory and a query string str. The task is to implement search query for the phone directory. 
Run a search query for each prefix p of the query string str(i.e from  index 1 to str length) that prints all the distinct recommended contacts which have the same prefix as our query (p) in lexicographical order. 
NOTE: If there is no match between query and contacts , print "0".
Input:
1
3
geeikistest geeksforgeeks geeksfortest
geeips
Output:
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest geeksforgeeks geeksfortest
geeikistest
0
0

Explanation:
By running the query on contact list, we get, 
Suggestions based on "g" are:  geeikistest geeksforgeeks geeksfortest 
Suggestions based on "ge" are: geeikistest geeksforgeeks geeksfortest
Suggestions based on "gee" are: geeikistest geeksforgeeks geeksfortest
Suggestions based on "geei" are: geeikistest
No Results Found for "geeip", So print "0".
No Results Found for "geeips", So print "0".    
'''
class TrieNode:
    def __init__(self, data):
        self.data = data
        self.h = {}
        self.isterminal = False
    
class Trie:
    def __init__(self):
        self.__root = TrieNode('')
    
    def get_trie_node(self):
        return self.__root
        
    def insert(self, word):
        
        temp = self.get_trie_node()
        for ch in word:
            if ch not in temp.h:
                child = TrieNode(ch)
                temp.h[ch] = child
                temp = child
            else:
                temp = temp.h[ch]
                
        temp.isterminal = True
    
    def suggestions_util(self, node, prefix):
        if node.isterminal:
            print(prefix, end = ' ')
        
        for code in range(ord('a'), ord('z')+1):                    # use it for lexiographically
            ch = chr(code)
            if ch in node.h:
                self.suggestions_util(node.h[ch], prefix + ch)

    def suggestions(self, search_word):
       
        node = self.get_trie_node()
        
        prefix = ''
        n = len(search_word)
        for ch in search_word:
            if ch in node.h:
                n -= 1
                prefix += ch                          # append each character 
                node = node.h[ch]                     # advance pointer to that node and call on further tree recursively for suggestions
                self.suggestions_util(node, prefix)
                print()
            else:                                     # if any word is not matched means after that continuous same words break
                break
        while n:
            print(0)
            n -= 1
    
def implement(words, n, search_word):
    t = Trie()
    for word in words:
        t.insert(word)
    
    t.suggestions(search_word)
    
t = int(input())
while t:
    n = int(input())
    words = input().split()
    search_word = input()
    implement(words, n, search_word)
    t -= 1