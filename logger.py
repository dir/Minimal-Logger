import time

# Minimal logger written by @R8T3D

class logger(object):
	def log(self, msg):
		currenttime = time.strftime("%H:%M:%S")
		print "[%s] %s" % (currenttime, str(msg))
