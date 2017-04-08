import numpy as np

class MemoryScheduler(object):

	MinimumEFactor = 1.3
	MinimumIntervl = 1
	MinimumRepetit = 1

	def __init__(self):
		pass

	@staticmethod
	def calculate_int_reps(qual, EF, reps, i_old):
		"""Calculate the interval and effective repetitions values.

		I(1) := 1
		I(2) := 2
		I(n) := I(n-1) * EF
		"""

		i_new = MinimumIntervl
		r_new = MinimumRepetit
		noise = np.random.normal(0, 1)

		if reps <= 1 or  qual < 3:              
			i_new = MinimumIntervl
			r_new = if qual < 3 MinimumRepetit else reps + 1

		if reps == 2 and qual > 2:
			i_new = 2 + noise
			r_new = reps + 1

		if reps >= 3 and qual > 2:
			i_new = i_old * EF + noise
			r_new = reps + 1

		return int(max(MinimumIntervl, i_new)), int(max(MinimumRepetit, r_new))

	@staticmethod
	def calculate_e_factor(qual, EF, priority):
		"""Calculate the easiness memorization factor value.

		EF':=EF-0.8+0.28*q-0.02*q*q
		EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))
		note for q=4, EF does not change.
		"""

		e_clc = EF - 0.8 + 0.28 * qual - 0.02 * qual * qual
		return min(MinimumEFactor, e_clc / priority)

	@staticmethod
	def fight_interference(): 
		pass
