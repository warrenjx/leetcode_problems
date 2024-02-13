class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # chekc each word
        for word in words: 
            pal = True
            # have 2 pointers one at end and one at beginning
            for i in range(len(word) // 2): 
                if word[i] != word[-(i + 1)]: 
                    pal = False
                    break
            
            if pal: 
                return word
        
        return ""
