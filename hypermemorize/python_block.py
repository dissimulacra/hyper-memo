import numpy as np
import os
import subprocess

class PythonBlock(MemoryBlock):

	def __init__(self, question, response, priority=1.2):
		MemoryBlock.__init__(self, question, response, priority=priority)

	def show_question(self):
		# pygmentize
		self.__pygmentizit(self.question)

	def show_response(self):
		# pygmentize
		self.__pygmentizit(self.response)

	def __pygmentizit(self, content, tmp_dir='tmpPythonBlock', tmp_pyc='tmp.py'):
		tmp_directory = tmp_dir
		tmp_pyth_file = tmp_dir + tmp_pyc
		os.mkdir(tmp_directory)
		with open(tmp_pyth_file, 'wb') as f:
			f.write(content)
		_ = subprocess.call(['pygmentize', tmp_pyth_file])
		os.remove(tmp_pyth_file)
		os.rmdir(tmp_directory)
