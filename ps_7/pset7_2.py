import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

# Load data
data = pd.read_csv(r"C:\Users\HP-ENVY\Downloads\survey.csv")

# Convert data to numpy arrays
xs = data['age'].to_numpy()
ys = data['recognized_it'].to_numpy()
x_sort = np.argsort(xs)
xs = xs[x_sort]
ys = ys[x_sort]

# Define logistic function
def p(x, beta_0, beta_1):
    return 1 / (1 + np.exp(-(beta_0 + beta_1 * x)))

# Define log likelihood function
def log_likelihood(beta, xs, ys):
    beta_0 = beta[0]
    beta_1 = beta[1]
    epsilon = 1e-16
    l_list = [ys[i] * np.log(p(xs[i], beta_0, beta_1) / (1 - p(xs[i], beta_0, beta_1) + epsilon))
              + np.log(1 - p(xs[i], beta_0, beta_1) + epsilon) for i in range(len(xs))]
    ll = np.sum(np.array(l_list), axis=-1)
    return -ll  # return log likelihood

# Optimize to find maximum likelihood values
result = optimize.minimize(log_likelihood, x0=[0, 0], args=(xs, ys))

# Calculate Hessian matrix
hess_inv = result.hess_inv
var = result.fun / (len(ys) - len(result.x))
cov_matrix = hess_inv * var

# Extract errors
error_beta_0 = np.sqrt(cov_matrix[0, 0])
error_beta_1 = np.sqrt(cov_matrix[1, 1])

# Print results
print('Maximum Likelihood Values:')
print(f'  beta_0: {result.x[0]}, beta_1: {result.x[1]}')
print('Formal Errors:')
print(f'  error_beta_0: {error_beta_0}, error_beta_1: {error_beta_1}')
print('Covariance Matrix:')
print(cov_matrix)

# Plot logistic model
x_prediction = 50
beta_0 = np.linspace(-5, 5, 100)
beta_1 = np.linspace(-5, 5, 100)
beta_meshgrid = np.meshgrid(beta_0, beta_1)
p_grid = p(x_prediction, *beta_meshgrid)

plt.pcolormesh(*beta_meshgrid, p_grid)
plt.colorbar()
plt.xlabel(r'$\beta_0$', fontsize=16)
plt.ylabel(r'$\beta_1$', fontsize=16)
plt.title(r'$p(y_i|x_i=50,\beta_0, \beta_1)$', fontsize=16)
plt.scatter([result.x[0]], [result.x[1]], color='red', marker='x', label='Max Likelihood')
plt.legend()
plt.show()

# Plot logistic model with the maximum likelihood values
plt.plot(xs, p(xs, *result.x), label='Logistic Model')
plt.scatter(xs, ys, color='blue', marker='o', label='Data')
plt.xlabel('Age')
plt.ylabel('Recognized IT')
plt.legend()
plt.show()
