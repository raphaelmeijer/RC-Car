class Sensors:
	doneCrossing 			= False
	hasDestination 			= ""
	direction  				= "FORWARD"
	wait_for_destination	= False
	def getDirection(self):
		return self.direction
	def setCarDirection(self, pins ):
		if( pins[0] == 0 and pins[1] == 0 and pins[2] == 0 ):
			print "DETECTED: Crossing"
			# Check if we have a destination
			if( self.hasDestination ):
				print "NOTICED: We have a destination"
				# we might have a crossing - specify
				if( self.doneCrossing ):
					print "DETECTED: Arrived at the the house"
					# we can stop
					self.direction = "STOP"
				else:
					# we have not done a crossing - go to destination
					if( self.hasDestination == "A" ):
						print "NOTICED: B is LEFT"
						self.direction = "LEFT"
					elif( self.hasDestination == "B" ):
						print "NOTICED: B is FORWARD"
						self.direction 				= "FORWARD"
						self.wait_for_destination	= True 
					elif( self.hasDestination == "C" ):
						print "NOTICED: C is RIGHT"
						self.direction = "RIGHT"
			else:
				print "DETECTED: No destination, just go forward!"
				# Just go forward...
				self.direction = "FORWARD"
				# wait for variable
				self.wait_for_destination 	= True
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 1 ): 
			print "DETECTED: Direction set to FORWARD"
			self.wait_for_destination 	= False
			self.direction   			= "FORWARD"
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 0 and self.wait_for_destination == False ):
			print "DETECTED: Direction set to SLOW_RIGHT"
			self.direction   = "SLOW_RIGHT"
		elif( pins[0] == 1 and pins[1] == 1 and pins[2] == 0 and self.wait_for_destination == False ):
			print "DETECTED: Direction set to RIGHT"
			self.direction   = "RIGHT"
		elif( pins[0] == 0 and pins[1] == 0 and pins[2] == 1 and self.wait_for_destination == False ):
			print "DETECTED: Direction set to SLOW_LEFT"
			self.direction   = "SLOW_LEFT"
		elif( pins[0] == 0 and pins[1] == 1 and pins[2] == 1 and self.wait_for_destination == False ):
			print "DETECTED: Direction set to LEFT"
			self.direction   = "LEFT"