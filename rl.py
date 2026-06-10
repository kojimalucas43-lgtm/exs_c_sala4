import numpy as np


def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def compute_cost(x, y, theta):
  m = len(y)
  h = sigmoid(x @ theta)
  epsilon = 1e-5

  return (-1/m) * (y.T @ np.log(h + epsilon) + (1 - y).T @ np.log(1 - h + epsilon))

def gradient_descent(x, y, theta, alpha, iterations):
  m = len(y)
  for i in range(iterations):
    h = sigmoid(x @ theta)
    gradient = (1/m) * (x.T @ (h - y))
    theta -= alpha * gradient
  return theta

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([[0], [0], [1], [1], [1]])

x_b = np.hstack([np.ones((x.shape[0], 1)), x])

theta = np.zeros((x_b.shape[1], 1))

alpha = 0.1
iterations = 1000

theta = gradient_descent(x_b, y, theta, alpha, iterations)
print('Parâmetros aprendidos: ', theta)

def predict(x, theta):
  x_b = np.hstack([np.ones((x.shape[0], 1)), x])
  probabilities = sigmoid(x_b @ theta)
  return probabilities >= 0.5


x_new = np.array([[1.5], [3.5]])
predictions = predict(x_new, theta)
print('Previsões: ', predictions)