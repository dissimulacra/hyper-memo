import numpy as np

class PythonBlock(MemoryBlock):

	def __init__(self, content_q, content_a, importance=1.0):
		MemoryBlock.__init__(self, content_q, content_a, importance=1.2)

	def show_content_q(self):
		# TODO: pygmentize
		pass

	def show_content_a(self):
		# TODO: pygmentize
		pass

	def update_memory_factors(self, response_quality):
		# TODO: super method, then add noise
		pass
		