import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = np.mean(matrix,axis=1) if mode != 'column' else np.mean(matrix,axis=0)
	return means