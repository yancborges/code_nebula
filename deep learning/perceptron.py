from random import uniform, randint

def sign(n):
	if(n >= 0):
		return 1
	else:
		return -1


class perceptron:

	def __init__(self):
		
		self.weights = []
		self.lr = 0.1
		
		for i in range(2):
			self.weights.append(uniform(-1,1))


	def predict(self, inputs):
		p = 0
		for i in range(len(self.weights)):
			p += inputs[i] * self.weights[i]

		return sign(p)

	def train(self, inputs, label):
		y = self.predict(inputs)
		error = label - y

		for i in range(len(self.weights)):
			self.weights[i] += error * inputs[i] * self.lr

if __name__ == '__main__':

	def oddeven(n):
		resp = 0
		for i in range(len(n)):
			if(n[i]/2 != int(n[i]/2)):
				resp += 1
		if(resp > 0):
			return -1
		else:
			return 1

	inputs = []
	size = 100
	for i in range(size):
		inputs.append([randint(0,9),randint(0,9)])

	p = perceptron()
	
	right = 0
	wrong = 0

	for i in inputs:
		p.train(i, oddeven(i))
		y = p.predict(i)
		print(i, end='')
		if( y == oddeven(i) ):
			right += 1
			print(' *')
		else:
			wrong += 1
			print('')
	print('[%d/%d]' %(right,wrong))






