class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sol = ""

        for idx in range(len(strs[0])): 
            curr = strs[0][idx]
            broken = False
            for i in range(1, len(strs)): 
                if idx >= len(strs[i]): 
                    broken = True
                    break
                elif strs[i][idx] != curr: 
                    broken = True
                    break

            if broken:
                break
            else: 
                sol += curr
            
        return sol
