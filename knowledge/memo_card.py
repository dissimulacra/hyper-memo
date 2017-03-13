import numpy as np

class MemoCard(object):

	def __init__(self):
		self.content_q         = None
		self.content_a         = None

		self.e_factor          = 1.3
		self.interval          = 0
		self.repetition        = 0

		self.remaining_time_ts = 0
		self.interval_start_ts = 0

		self.history           = [] # responses, calculated_intervals, 
		                            # calculated_efactors, review_dates