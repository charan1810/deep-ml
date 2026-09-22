import numpy as np
def linear_regression_normal_equation(X_arr: list[list[float]], y_arr: list[float]) -> list[float]:
	# Your code here, make sure to round
		X=np.array(X_arr)
		y=np.array(y_arr)
		m=len(X)
		X_raw=np.c_[np.ones((m,1)),X]
		theta = np.linalg.inv(X.T @ X) @ X.T @ y

		# Round and return as list
		return np.round(theta,4).tolist()