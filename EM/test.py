import numpy as np
mean = (0, 0, 0)
cov = np.identity(3)
x = np.random.multivariate_normal(mean, cov, 10, 'raise')
print(x)
print(x.shape)