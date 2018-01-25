import time
import os, random
import pyttsx
class Sensors:
	doneCrossing 			= False
	hasDestination 			= "A" 
	startedCrossingAt		= 0
	endedCrossingAt			= 0
	direction  				= "FORWARD"
	wait_for_destination	= { 'SLOW_LEFT' : 0, 'FORWARD' : 0, 'SLOW_RIGHT' : 0 }
	timeout					= 0.25
	last_timeout_check		= 0
	last_random_destination	= { 'LEFT' : 0, 'FORWARD' : 0, 'RIGHT' : 0 }
	last_turn 				= ""
	
	def getDirection(self):
		return self.direction
	def setCarDirection( self, pins ):
		if( pins[0] == 0 and pins[1] == 0 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 and self.wait_for_destination['SLOW_RIGHT'] == 0 ):
			print "DETECTED: Crossing"
			# timestamp for crossing
			if( self.startedCrossingAt == 0 ):
				self.startedCrossingAt 	= time.time()
			# Check if we have a destination
			if( self.hasDestination != ''):
				print "NOTICED: We have a destination"
				# we might have a crossing - specify
				if( self.doneCrossing ):
					print "DETECTED: Arrived at house %s" % self.hasDestination
					#init.message= "You have arrived at your destination %s" % self.hasDestination
					# we can stop
					self.direction = "STOP" 
					# self.speakEnd()
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
				print "DETECTED: No destination, just go FORWARD!"
				# Just go 
				# self.direction	= self.direction.replace( "SLOW_", "" )
				self.direction	= "FORWARD"
			# wait for variable
			self.wait_for_destination[self.direction] 	= 1
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 1  and ( time.time() - self.startedCrossingAt > 1.5 or self.direction == 'FORWARD' ) ): 
			print "DETECTED: Direction set to FORWARD"
			# try to reset crossing direction
			for aDirection in self.wait_for_destination:
				# check if a pin has been activated
				if( self.wait_for_destination[aDirection] == 1 ):      
					# debug code
					self.endedCrossingAt = time.time()
					# let the us know we are resetting a destination
					print "Resetting tryout crossing for: %s" % aDirection
					print self.endedCrossingAt - self.startedCrossingAt
					# let us know we have done a crossing
					self.doneCrossing						= True;
					self.wait_for_destination[aDirection] 	= 0
			self.direction   						= "FORWARD"
		elif( pins[0] == 1 and pins[1] == 0 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to SLOW_RIGHT"
			self.direction   	= "SLOW_RIGHT"
			self.last_turn 		= self.direction
		elif( pins[0] == 1 and pins[1] == 1 and pins[2] == 0 and self.wait_for_destination['SLOW_LEFT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to RIGHT"
			self.direction   = "RIGHT"
			self.last_turn 		= self.direction
		elif( pins[0] == 0 and pins[1] == 0 and pins[2] == 1 and self.wait_for_destination['SLOW_RIGHT'] == 0 and self.wait_for_destination['FORWARD'] == 0 ):
			print "DETECTED: Direction set to SLOW_LEFT"
			self.direction   = "SLOW_LEFT"
			self.last_turn 		= self.direction
		elif( pins[0] == 0 and pins[1] == 1 and pins[2] == 1 and self.wait_for_destination['SLOW_RIGHT'] == 0 and self.wait_for_destination['FORWARD'] == 0):
			print "DETECTED: Direction set to LEFT"
			self.direction   = "LEFT"
			self.last_turn 		= self.direction
		elif( pins[0] == 1 and pins[1] == 1 and pins[2] == 1 ):
			if( ( self.last_turn == 'RIGHT' and self.direction == 'LEFT' ) or ( self.last_turn == 'LEFT' and self.direction == 'RIGHT' ) ):
				self.direction 	= "FORWARD"
			elif( self.last_turn != '' ):
				# do last direction but fast!
				self.direction 	= self.last_turn.replace("SLOW_", "") 
				# empty var
				self.last_turn 	= ''
		return self.direction
