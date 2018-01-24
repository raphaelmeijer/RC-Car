class Sequence:
    FORWARD 	= [True, True] # On forward, we can use both wheels
    LEFT    	= [False, True] # On left, we can use only the right wheel
    SLOW_LEFT 	= [False, True] # On left, we can use only the right wheel
	RIGHT   	= [True, False] # On right, we can use only the left wheel
    SLOW_RIGHT  = [True, False] # On right, we can use only the left wheel
	
	# get the sequence
    def getSequence( self, name ):
	    return self[name]
  