'''
https://practice.geeksforgeeks.org/problems/trie-insert-and-search/0
Trie is an efficient information retrieval data structure. Use this data structure to store Strings and search strings. Your task is to use the TRIE data structure and search the given string A. If found print 1 else 0.
Expected Time Complexity: O(N * WORD_LEN + A_LEN).
Expected Auxiliary Space: O(N * WORD_LEN).
'''

class TrieNode:
    def __init__(self, data):
        self.data = data
        self.h = {}
        self.isTerminal = False

class Trie:

    def __init__(self):
        self.__root = TrieNode('')                              # keep root node with blank data

    def get_trie_node(self):
        return self.__root
    
    def insert(self, word):

        temp = self.get_trie_node()                                  
        for ch in word:
            if ch not in temp.h:                            # if character is not child of current node
                child = TrieNode(ch)                            # create node
                temp.h[ch] = child                          # append child to current node's map
                temp = child                                # advance pointer to child node so that next character can be inserted
            else:
                temp = temp.h[ch]                           # if character is present then just advance our pointer

        temp.isTerminal = True                              # set isterminal of end character as true to mark the ending of 1 word
    
    def search(self, word):

        temp = self.get_trie_node()                                  # start from root node
        for ch in word:
            if ch not in temp.h:                            # character is not present as child, means word is not present
                return False 
            else:
                temp = temp.h[ch]                           # if character present, then just advance our pointer
        return temp.isTerminal                              # if word is found, then check it is terminal

    def delete(self, word):

        temp = self.get_trie_node()                          
        for ch in word:
            if ch not in temp.h:
                return 
            else:
                temp = temp.h[ch]
        temp.isTerminal = False                             # to delete, just mark terminal node as false
    
    def update(self, oldstring, newstring):
        self.delete(oldstring)                              # update a string, first delete old string then insert new string
        self.insert(newstring)
        
def implementation(words, search_word):
    
    t = Trie()
    for word in words:
        t.insert(word)
    
    if t.search(search_word):
        print(1)
    else:
        print(0)
    
t = int(input())
while t:
    n = int(input())
    words = input().split()
    search_word = input()
    implementation(words, search_word)
    t -= 1