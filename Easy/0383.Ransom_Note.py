class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran_dic = {}
        mag_dic = {}

        # make dictionaries to keep track of how many of each character
        for char in ransomNote: 
            if char in ran_dic: 
                ran_dic[char] += 1
            else: 
                ran_dic[char] = 1
        
        for char in magazine: 
            if char in mag_dic: 
                mag_dic[char] += 1
            else: 
                mag_dic[char] = 1

        # make sure there are enough characters in the magazine for the ransom note
        for char, num in ran_dic.items(): =
            if char in mag_dic: 
                if num > mag_dic[char]: 
                    return False
            else: 
                return False
        
        return True
