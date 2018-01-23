class Sensors:
    
    direction   = "FORWARD"
    SensPins    = [14,15,18]
    SensValues  = [0,0,0]
    GPIO        = False
    def __init__( self, GPIO ):
        self.GPIO = GPIO
	while True:
            # try to echo the pins
            for pin in self.SensPins:
                self.SensValues[counter] = self.GPIO.input( pin )
                counter = counter + 1
            
            counter = 0

            self.setCarDirection( SensValues )
    def getDirection(self ):
        return self.direction
    def setCarDirection(self, pins ):
        if( pins[0] == 1 and pins[1] == 0 and pins[2] == 1 ):
           self.direction   = "FORWARD"
        elif( pins[0] == 1 and ( pins[1] == 0 or pins[1] == 1 ) and pins[2] == 0 ):
           self.direction   = "LEFT"
        elif( pins[0] == 0 and ( pins[1] == 0 or pins[1] == 1 ) and pins[2] == 1 ):
           self.direction   = "RIGHT"
    
