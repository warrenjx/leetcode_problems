class Trie(object):

    def __init__(self):
        # implement trie with nested dictionaries
        self.trie = {}


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.trie
        # add characters to trie in a nested fashion
        for char in word: 
            if char not in curr:  
                curr[char] = {}

            curr = curr[char]
        
        # terminator character to differentiate words and prefix
        curr["0"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.trie
        # same as search but checking if char is in rather than adding char
        for char in word: 
            if char not in curr: 
                return False
            
            curr = curr[char]
        
        # if no terminator character, then word itself isn't in it
        if "0" not in curr: 
            return False

        return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.trie
        # same as search
        for char in prefix: 
            if char not in curr: 
                return False
            
            curr = curr[char]

        # no terminator required though

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
