class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []
        # sorting makes it easier to avoid duplicates
        candidates.sort()

        stack = deque()
        # format: current total, current path, index to start building path on
        stack.append((0, [], 0))

        while stack: 
            sm, path, idx = stack.pop()

            if sm == target: 
                sol.append(path)
            elif sm > target: 
                continue
            
            for i in range(idx, len(candidates)): 
                # skip identical numbers to avoid duplicates
                if i > idx and candidates[i] == candidates[i - 1]: 
                    continue

                stack.append((sm + candidates[i], path + [candidates[i]], i + 1))
        
        return sol
