class WordDictionary(object):

    def __init__(self):
        # uses a dictionary to implement trie
        self.trie = {}

    def addWord(self, word):
        trie = self.trie
        
        # if char in trie, go to it, if not add it to trie then go to it
        for c in word:
            trie = trie.setdefault(c, {})
        
        # marks the end of the word in the trie
        trie['word'] = word
        
    def search(self, word):
        return self.helper(self.trie, word)
    
    def helper(self, trie, word):
        # only reason for word to be empty if it was at end of path in trie, thus look for 'word'
        if not word:
            return True if trie.get('word') else False
        
        # wildcard match, '.' can be anything, so recursively call on all branches of trie
        if word[0] == '.':      
            for c in trie:
                if c != 'word' and self.helper(trie[c], word[1:]):
                    return True
        
        # check of charcter is in trie then move down trie path if it is
        elif word[0] in trie:
            return self.helper(trie[word[0]], word[1:])
        
        # if none of above conditions are met
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
