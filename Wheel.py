def Wheel():
    Sequence        = [
        [1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1]
    ]
    StepCount 	    = 0 
    StepCounter     = 0    
    StepPins        = []
    StepDirection   = 1
    SpeedDir        = 0

    def __init__(self, stepPins, stepDirection, speedDir ):
        self.StepPins       = stepPins
        self.StepDirection  = stepDirection
        self.StepCount      = len(self.Sequence)
        self.SpeedDir       = speedDir

    def turnWheel( self ):
        Speed   = getattr( Sequence, Sensors.getDirection() )
        
        #while loop
        while True:
            #for loop for pins
            for pin in range(0,4):
                # the required pins
                xpin=  self.StepPins[pin]# Get GPIO
                #turn it on or off based on sequence
                if self.Sequence[self.StepCounter][pin]!=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            # we need this because ?
            self.StepCounter += self.StepDirection

            # If we reach the end of the sequence
            # start again
            if (self.StepCounter>=self.StepCount):
                self.StepCounter = 0
            if (self.StepCounteL<0):
                self.StepCounter = StepCount+StepDirL
                
            time.sleep(Speed[self.speedDir])