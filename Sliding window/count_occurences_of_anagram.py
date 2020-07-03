'''
https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams/0
Given a word S and a text C. Return the count of the occurences of anagrams of the word in the text.
Input:
2
forxxorfxdofr
for
aabaabaa
aaba

Output:
3
4

Explaination:
for, orf and ofr appears in the first test case and hence answer is 3.
'''

# keep 2 map each for word and text
# window length = len of word
# we keep on matching both maps for checking anagrams at each point

def count_occurences(text, word):
    hw = {}
    ht = {}
    count = 0
    
    # put all characters of word in its map
    for ch in word:
        if ch in hw:
            hw[ch] += 1
        else:
            hw[ch] = 1
    
    # put starting characters of text equal to window size in map
    k = len(word)
    n = len(text)
    for i in range(k):
        ch = text[i]
        if ch in ht:
            ht[ch] += 1
        else:
            ht[ch] = 1
    count += (hw==ht)
    
    # now keep adding and removing character at each point from map and check both maps are equal and increment count
    for i in range(k, n):
        ht[text[i-k]] -= 1
        if ht[text[i-k]] == 0:
            del ht[text[i-k]]
        ch = text[i]
        if ch in ht:
            ht[ch] += 1
        else:
            ht[ch] = 1
        count += (hw==ht)
    print(count)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        text = input()
        word = input()
        count_occurences(text, word)
        t -= 1