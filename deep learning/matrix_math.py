import random

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
		if(type(n) == type(self)):
			if(self.rows == n.rows and self.cols == n.cols):
				for i in range(self.rows):
					for j in range(self.cols):
						self.matrix[i][j] *= n.matrix[i][j]
			elif(self.rows == n.cols and self.cols == n.rows):
				new_matrix = Matrix(self.rows, n.cols)
				for i in range(new_matrix.rows):
					for j in range(new_matrix.cols):
						s = 0
						for k in range(self.matrix.cols):
							s += self.matrix[i][k] * n.matrix[k][j]
						new_matrix.matrix[i][j] = s
				return new_matrix


		elif(type(n) == 'int'):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] *= n

	def add(self, n):
		if(type(n) == type(self)):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] += n.matrix[i][j]
		elif(type(n) == 'int'):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] += n

	def randomize(self):
		for i in range(self.rows):
			for j in range(self.cols):
				self.matrix[i][j] *= random.randint(0,9)