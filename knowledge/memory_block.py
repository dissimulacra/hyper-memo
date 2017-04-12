import numpy as np
import time

class MemoryBlock(object):

	InitialEFactor = 2.5

	def __init__(self, question=None, response=None, priority=1.0):
		# should internal state just be a dict? easier to publish state
		self.redundid = int(time.time() - 365.25 * 10 * 24 * 60 * 60)
		self.question = question
		self.response = response
		self.priority = priority
		
		self.repetits = 0
		self.e_factor = InitialEFactor
		self.interval = 0
		self.start_ts = 0

	def show_question(self):
		# override for sophisticated blocks
		print self.question

	def show_response(self):
		# override for sophisticated blocks
		print self.response

	def inspect(self):
		# rarely used outside of writing db-push data
		internal_state = {'redundid': self.redundid,
						  'question': self.question,
						  'response': self.response,
						  
						  'priority': self.priority,
						  
						  'repetits': self.repetits,
						  'e_factor': self.e_factor,
						  'interval': self.interval,
						  'start_ts': self.start_ts}
		return internal_state

	def initize(self, state):
		# rarely used outside of storing db-pull data
		# TODO: add error handling
		self.redundid = state['redundid']
		self.question = state['question']
		self.response = state['response']
		
		self.priority = state['priority']
		
		self.repetits = state['repetits']
		self.e_factor = state['e_factor']
		self.interval = state['interval']
		self.start_ts = state['start_ts']

	def update_memory(self, e_factor, interval, repetits):

		self.repetits  = repetits
		self.e_factor  = e_factor
		self.interval  = interval
		self.start_ts  = int(time.time())
