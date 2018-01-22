class Sensors:
    
    direction   = "FORWARD";

    def getDirection( pin ):
        return direction
    def setDirection( pins ):
        if( pins[0] == 0 && pins[1] == 0 && pins[2] == 0 )
            direction   = "FORWARD"
        else if( pins[0] == 1 && pins[1] == 0 && pins[2] == 0 )
            direction   = "LEFT"
        else if( pins[0] == 1 && pins[1] == 1 && pins[2] == 0 )
            direction   = "RIGHT"
    
