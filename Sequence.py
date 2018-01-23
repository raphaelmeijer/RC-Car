class Sequence:
    FORWARD = [0.0005, 0.0005]
    LEFT    = [1, 0.0005]
    RIGHT   = [0.0005, 1]
    SLOW_LEFT 	= [1, 0.0005]
    SLOW_RIGHT  = [0.0005, 1]
    def getSequence( self, name ):
	    return self[name]
