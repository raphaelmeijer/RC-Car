class Sensors:
	doneCrossing 			= False
	hasDestination 			= "C"
	direction  				= "FORWARD"
	wait_for_destination	= { 'SLOW_LEFT' : 0, 'FORWARD' : 0, 'SLOW_RIGHT' : 0 }
	
	def getDirection(self):
		return self.direction
	def setCarDirection( self, pins ):
		print self.wait_for_destination
		if( pins[0] == 0 and pins[1] == 0 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 and self.wait_for_destination['FORWARD'] == 0):
			print "DETECTED: Crossing"
			# Check if we have a destination
			if( self.hasDestination != ''):
				print "NOTICED: We have a destination"
				# we might have a crossing - specify
				if( self.doneCrossing ):
					print "DETECTED: Arrived at house %s" % self.hasDestination
					# we can stop
					self.direction = "STOP"
					return self.direction
				else:
					# we have not done a crossing - go to destination
					if( self.hasDestination == "A" ):
						print "NOTICED: A is LEFT"
						self.direction 				= "SLOW_LEFT"
					elif( self.hasDestination == "B" ):
						print "NOTICED: B is FORWARD"
						self.direction 				= "FORWARD"
						# self.wait_for_destination	= 1 
					elif( self.hasDestination == "C" ):
						print "NOTICED: C is RIGHT" 
						self.direction 				= "SLOW_RIGHT"
			else:
				# Just let us know that we do not have a destination
				print "DETECTED: No destination, just go %s!" % self.direction
				# Just go forward...
				self.direction = "FORWARD"
			# wait for variable
			self.wait_for_destination[self.direction] 	= 1
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 1 ): 
			print "DETECTED: Direction set to FORWARD"
			# try to reset crossing direction
			for aDirection in self.wait_for_destination:
				# check if a pin has been activated
				if( self.wait_for_destination[aDirection] == 1 ):
					# let the us know we are resetting a destination
					print "Resetting tryout crossing for: %s" % aDirection
					# let us know we have done a crossing
					self.doneCrossing						= True;
					self.wait_for_destination[aDirection] 	= 0
			self.direction   						= "FORWARD"
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to SLOW_RIGHT"
			self.direction   = "SLOW_RIGHT"
		elif( pins[0] == 1 and pins[1] == 1 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to RIGHT"
			self.direction   = "RIGHT"
		elif( pins[0] == 0 and pins[1] == 0 and pins[2] == 1 and self.wait_for_destination['SLOW_RIGHT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to SLOW_LEFT"
			self.direction   = "SLOW_LEFT"
		elif( pins[0] == 0 and pins[1] == 1 and pins[2] == 1 and self.wait_for_destination['SLOW_RIGHT'] == 0 and self.wait_for_destination['FORWARD'] == 0):
			print "DETECTED: Direction set to LEFT"
			self.direction   = "LEFT"
		
		return self.direction