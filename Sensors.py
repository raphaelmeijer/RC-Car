class Sensors:
    
    direction   = "FORWARD";

    def getDirection(self ):
        return self.direction
    def setCarDirection(self, pins ):
        if( pins[0] == 1 and pins[1] == 0 and pins[2] == 1 ):
           self.direction   = "FORWARD"
        elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 0 ):
           self.direction   = "SLOW_RIGHT"
        elif( pins[0] == 1 and pins[1] == 1 and pins[2] == 0 ):
           self.direction   = "RIGHT"
        elif( pins[0] == 0 and pins[1] == 0 and pins[2] == 1 ):
           self.direction   = "SLOW_LEFT"
        elif( pins[0] == 0 and pins[1] == 1 and pins[2] == 1 ):
           self.direction   = "LEFT"
    
