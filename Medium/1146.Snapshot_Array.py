class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.id = 0
        # format is [[snap_id, val], ...]
        self.snaps = [[[0, 0]]] * length
        for i in range(length): 
            self.snaps[i] = [[0, 0]]
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.snaps[index][-1][0] != self.id: 
            self.snaps[index].append([self.id, val])
        else: 
            self.snaps[index][-1][1] = val
        

    def snap(self):
        """
        :rtype: int
        """
        self.id += 1
        
        return self.id - 1


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # binary search for best option: n most <= snap_id
        lo = 0
        hi = len(self.snaps[index]) - 1

        while lo <= hi: 
            mi = (hi + lo) // 2

            if self.snaps[index][mi][0] == snap_id: 
                return self.snaps[index][mi][1]
            elif self.snaps[index][mi][0] > snap_id: 
                hi = mi - 1
            else: 
                lo = mi + 1

        return self.snaps[index][hi][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
