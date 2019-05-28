class Matrix:

	def __init__(self, rows, cols):

		self.rows = rows
		self.cols = cols
		self.matrix = []

		for i in range(self.rows):
			self.matrix[i] = []
			for j in range(self.cols):
				self.matrix[i][j] =  0


	def mult(self, n):
		for i in range(self.rows):
			for j in range(self.cols):
				self.matrix[i][j] *= n

	def add(self, n):
		for i in range(self.rows):
			for j in range(self.cols):
				self.matrix[i][j] += n
