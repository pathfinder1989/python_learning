class student(object):
	"""docstring for student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s : %s' % (self.name , self.score))
		


bart = student('kang', 59)
lisa = student('bo', 60)

bart.print_score()
lisa.print_score()