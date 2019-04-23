from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):

		random.seed(1)
		self.synaptic_weights = 2 * random.random((3,1)) - 1

	def __sigmoid(self, x):
		return 1/(1 + exp(-x))

	def __sigmoid_derivative(self, x):
		return x * (1 - x)

	def train(self, training_set_inputs, training_set_outputs, number_of_training_interations):
		for interation in range(number_of_training_interations):
			
			output = self.predict(training_set_inputs)
			error = training_set_outputs - output
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
			self.synaptic_weights += adjustment


	def predict(self, inputs):
		return self.__sigmoid(dot(inputs, self.synaptic_weights))




if (__name__ == '__main__'):

	neural_net = NeuralNetwork()

	print('Random starting synaptic wights:')
	print(neural_net.synaptic_weights)

	training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
	training_set_outputs = array([[0, 1, 1, 0]]).T

	neural_net.train(training_set_inputs,training_set_outputs,10000)

	print('New synaptic weights after training:')
	print(neural_net.synaptic_weights)

	print('Predicting:')    
	print(neural_net.predict(array([1,0,0])))
