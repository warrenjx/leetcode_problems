class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # creates tuple of form: (sorted_string, original_string)
        for i in range(0, len(strs)): 
            strs[i] = (''.join(sorted(strs[i])), strs[i])

        # creates dict with keys for each sorted_string, value is list
        hashmap = {}
        for s in strs: 
            hashmap[s[0]] = []

        # adds original_string's to lists with same sorted_string
        for s in strs: 
            hashmap[s[0]].append(s[1])

        return hashmap.values()