class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort by start point to make algorithm simple
        points.sort(key=lambda x:x[0])

        sol = 0
        # overlap represents the range where you can throw a dart and pop baloons
        overlap = points[0]
        for i in range(1, len(points)): 
            # if current balloon overlaps with the current overlap
            if points[i][0] <= overlap[1]: 
                # overlap should be shrinking or equal, never growing
                overlap[0] = max(overlap[0], points[i][0])
                overlap[1] = min(overlap[1], points[i][1])
            else: # not overlapping, pop current overlap and set new one
                sol += 1
                overlap = points[i]

        # have to do + 1 to account for the last overlap/balloon
        return sol + 1
