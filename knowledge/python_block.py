import numpy as np

class PythonBlock(MemoryBlock):

	def __init__(self, content_q, content_a, importance=1.0):
		MemoryBlock.__init__(self, content_q, content_a, importance=1.2)

	def show_question(self):
		# pygmentize
		print self.question

	def show_response(self):
		# pygmentize
		print self.response

	def inspect_block(self):
		internal_state = {k:v for }

	def initize_block(self):
		pass

	def update_memory(self, response_quality):
		# TODO: super method, then add noise
		pass
