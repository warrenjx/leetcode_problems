class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        # grid properties
        self.wid = width
        self.hgt = height

        # circumference needs to be adjusted because of how the robot moves
        self.circ = 2 * width + 2 * height - 4

        # initial robot properties
        self.pos = [0, 0]
        self.dir = "East"
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        # cut out full rotations from number of steps
        if (num > self.circ): 
            num %= self.circ
            
            # if do only full rotation from a corner, adjust direction of robot
            if (num == 0): 
                # change direction to the incoming direction
                if (self.pos == [0, 0]): 
                    self.dir = "South"
                elif (self.pos == [self.wid - 1, 0]): 
                    self.dir = "East"
                elif (self.pos == [self.wid - 1, self.hgt - 1]): 
                    self.dir = "North"
                elif (self.pos == [0, self.hgt - 1]): 
                    self.dir = "West"

        # if doing a partial rotation
        while (num > 0): 
            # diff specific behavior for each direction, same general trend
            if (self.dir == "East"):
                if ((self.pos[0] + num) >= self.wid): # if a direction change is needed
                    # change to next counterclockwise direction
                    self.dir = "North"
                    # subtract number of steps used to get to to next corner
                    num = self.pos[0] + num - self.wid + 1
                    # reenter loop with now updated steps and direction
                    self.pos[0] = self.wid - 1 
                else: # no direction change
                    # just increment position in the current direction
                    self.pos[0] += num
                    num = 0
            elif (self.dir == "West"): 
                if ((self.pos[0] - num) < 0): 
                    self.dir = "South"
                    num = abs(self.pos[0] - num)
                    self.pos[0] = 0
                else: 
                    self.pos[0] -= num
                    num = 0
            elif (self.dir == "North"): 
                if ((self.pos[1] + num) >= self.hgt): 
                    self.dir = "West"
                    num = self.pos[1] + num - self.hgt + 1
                    self.pos[1] = self.hgt - 1 
                else: 
                    self.pos[1] += num
                    num = 0
            elif (self.dir == "South"): 
                if ((self.pos[1] - num) < 0): 
                    self.dir = "East"
                    num = abs(self.pos[1] - num)
                    self.pos[1] = 0
                else: 
                    self.pos[1] -= num
                    num = 0


    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.pos


    def getDir(self):
        """
        :rtype: str
        """
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
