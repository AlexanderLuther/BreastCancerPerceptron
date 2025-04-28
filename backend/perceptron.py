import numpy as np

class Perceptron:

    def __init__(self, num_inputs):
        self.__errors_per_epoch = []
        self.__weights = np.zeros(num_inputs)
        self._bias = 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.__weights) + self._bias
        return self.__step_function(summation)

    def train(self, training_inputs, expected_outputs, epochs, learning_rate):
        for epoch in range(epochs):
            total_error = 0
            for inputs, expected_output in zip(training_inputs, expected_outputs):
                prediction = self.predict(inputs)
                error = expected_output - prediction
                self.__weights += learning_rate * error * inputs
                self._bias += learning_rate * error
                total_error += abs(error)
            self.__errors_per_epoch.append(total_error)

    def calculate_accuracy(self, inputs, expected_outputs):
        predictions = [self.predict(x) for x in inputs]
        correct = sum(p == o for p, o in zip(predictions, expected_outputs))
        accuracy = correct / len(expected_outputs)
        return accuracy

    def get_errors_per_epoch(self):
        return self.__errors_per_epoch

    def __step_function(self, x):
        return np.where(x >= 0, 1, 0)

