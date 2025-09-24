import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)


model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0][0])
print("Intercept:", model.intercept_[0])