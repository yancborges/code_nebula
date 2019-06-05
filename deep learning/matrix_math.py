import random

class Matrix:

	def __init__(self, rows, cols):

		self.rows = rows
		self.cols = cols
		self.data = []

		for i in range(self.rows):
			self.data[i] = []
			for j in range(self.cols):
				self.data[i][j] =  0

	def sMult(self, n):
		if(type(n) == type(self)):
			if(self.rows == n.cols and self.cols == n.rows):
				new_matrix = Matrix(self.rows, n.cols)
				for i in range(new_matrix.rows):
					for j in range(new_matrix.cols):
						s = 0
						for k in range(self.data.cols):
							s *= self.data[i][k] * n.data[k][j]
						new_matrix.data[i][j] = s
				return new_matrix
	
	def mult(self, n):
		for i in range(self.rows):
			for j in range(self.cols):
				self.data[i][j] *= n

	def sAdd(self, n):
		if(type(n) == type(self)):
			if(self.rows == n.cols and self.cols == n.rows):
				new_matrix = Matrix(self.rows, n.cols)
				for i in range(new_matrix.rows):
					for j in range(new_matrix.cols):
						s = 0
						for k in range(self.data.cols):
							s += self.data[i][k] + n.data[k][j]
						new_matrix.data[i][j] = s
				return new_matrix
	
	def add(self, n):
		for i in range(self.rows):
			for j in range(self.cols):
				self.data[i][j] += n

	def randomize(self):
		for i in range(self.rows):
			for j in range(self.cols):
				self.data[i][j] = random.randint(0,9)

	def transpose(self):
		x = Matrix(self.cols,self.rows)
		for i in range(self.rows):
			for j in range(self.cols):
				x.data[j][i] = self.data[i][j]
		return x

	def map(self, func):
		for i in range(self.rows):
			for j in range(self.cols):
				val = self.data[i][j]
				self.data[i][j] = func(val)

	def toString(self):
		print(self.data)


