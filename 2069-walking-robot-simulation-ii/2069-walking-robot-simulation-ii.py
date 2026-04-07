class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width
        self.h = height
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.pos = 0
        self.dir = "East"

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.pos = (self.pos + num) % self.perimeter
        
        # Bottom-left corner edge case (arriving from the Left edge)
        if self.pos == 0:
            self.dir = "South"
            return
            
        # FIX: Changed '<' to '<=' so corners retain the direction of approach
        if self.pos <= self.w - 1:
            self.dir = "East"
        elif self.pos <= (self.w - 1) + (self.h - 1):
            self.dir = "North"
        elif self.pos <= 2 * (self.w - 1) + (self.h - 1):
            self.dir = "West"
        else:
            self.dir = "South"

    def getPos(self):
        """
        :rtype: List[int]
        """
        if self.pos < self.w - 1:
            return [self.pos, 0]
        elif self.pos < (self.w - 1) + (self.h - 1):
            return [self.w - 1, self.pos - (self.w - 1)]
        elif self.pos < 2 * (self.w - 1) + (self.h - 1):
            return [(self.w - 1) - (self.pos - ((self.w - 1) + (self.h - 1))), self.h - 1]
        else:
            return [0, (self.h - 1) - (self.pos - (2 * (self.w - 1) + (self.h - 1)))]

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir