#!/usr/bin/env python
import os, random

def rndmp3 ():
	randomfile = random.choice(os.listdir("/home/pi/music/"))
	file = ' /home/pi/music/'+ randomfile
	os.system ('mplayer' + file)

rndmp3 ()