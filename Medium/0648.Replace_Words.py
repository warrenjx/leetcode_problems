class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # create the trie
        trie = {}
        for word in dictionary: 
            curr = trie
            for c in word: 
                if c not in curr: 
                    curr[c] = {}
                
                curr = curr[c]
            
            # delimeter marking an end of a root
            curr['_'] = word

        sol = []

        # turn sentence into list of words
        sentence = sentence.split(' ')
        # check each word for root matches
        for word in sentence: 
            curr = trie

            found = False
            # scan character by character
            for c in word: 
                if '_' in curr: # if end of a root is matched
                    found = True
                    break
                elif c in curr: # if still in process of matching a root
                    curr = curr[c]
                else: # no root match
                    break
            
            if found: # add the shortest root match
                sol.append(curr['_'])
            else: # add word if no match
                sol.append(word)

        return ' '.join(sol)
