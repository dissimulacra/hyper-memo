import numpy as np

class MemoryBlock(object):

	InitialEFactor = 2.5

	def __init__(self):
		self.redundid = None
		self.question = None
		self.response = None

		self.e_factor = InitialEFactor
		self.priority = 1.0
		self.interval = 0
		self.repetits = 0
		self.start_ts = 0

		# self.history           = {'responses':            [],
		# 						  'calculated_intervals': [],
		# 						  'calculated_efactors':  [],
		# 						  'review_dates':         []}



	def show_question(self):
		# override for sophisticated blocks
		print self.question

	def show_response(self):
		# override for sophisticated blocks
		print self.response

	def inspect_block(self):
		# rarely used outside of writing db-push data
		internal_state = {k:v for }

	def initize_block(self):
		# rarely used outside of storing db-pull data
		pass

	def update_memory(self, e_factor, interval, repetits):

		self.repetits  = repetits
		self.e_factor  = e_factor
		self.interval  = interval
		self.start_ts  = # timestamp

		# update self.history fields -> TODO: instead do a change record
