import numpy as np

class MemoryScheduler(object):

	def __init__(self):
		pass

	@staticmethod
	def calculate_interval():
		# add noise
		pass

	@staticmethod
	def calculate_e_factor():
		# add noise
		pass

		# self.repetition += 1
		# q  = response_quality
		# EF = self.e_factor

		# self.e_factor   = min(MinimumEFactor, 
		# 	                  (EF + (0.1 - (5.0 - q) * (0.08 + (5.0 - q) * 0.02))) / self.importance)

		# if self.repetition == 1 or  q < 3: # I(1) := 1
		# 	self.interval = 1
		# if self.repetition == 2 and q > 2: # I(2) := 2
		# 	self.interval = 2
		# if self.repetition >= 3 and q > 2: # I(n) := I(n-1) * EF
		# 	self.interval = self.interval * self.e_factor

		# self.interval_start_ts = 0