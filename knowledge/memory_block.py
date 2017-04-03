import numpy as np

class MemoryBlock(object):

	MinimumEFactor = 1.3
	InitialEFactor = 2.5

	def __init__(self, content_q, content_a, importance=1.0):
		self.content_q         = content_q
		self.content_a         = content_a

		self.e_factor          = InitialEFactor
		self.importance        = importance
		self.interval          = 0
		self.repetition        = 0

		#self.remaining_time_ms = 0
		self.interval_start_ts = 0

		self.history           = {'responses':            [],
								  'calculated_intervals': [],
								  'calculated_efactors':  [],
								  'review_dates':         []}

	def edit_content_factors(self, content_q=None, content_a=None, importance=None):
		if content_q:
			self.content_q  = content_q
		if content_a:
			self.content_a  = content_a
		if importance:
			self.importance = importance

	def show_content_q(self):
		# override for sophisticated blocks
		print self.content_q

	def show_content_a(self):
		# override for sophisticated blocks
		print self.content_a

	def update_memory_factors(self, response_quality):
		# override for sophisticated blocks
		self.repetition += 1

		self.e_factor   = # EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))
		self.interval   = # I(1):=1
						  # I(2):=6
						  # for n>2: I(n):=I(n-1)*EF

		self.interval_start_ts = 0

		# update self.history fields
