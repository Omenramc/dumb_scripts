import numpy as np 
from numba import njit, float32, float64, int16, int32, int64, complex64, complex128

@njit([float64(float32, int16, float32)],
	   error_model="numpy")
def lambertW(x_, max_iter=1000, eps=1e-3):
	w_ = np.random.normal(x_,1.0)
	for i in range(max_iter):
		w_new = (w_/(1+w_))*(1+np.log(x_/w_))
		if np.abs(w_ - w_new)<=eps:
			w_ = w_new
			break
		w_ = w_new
	return w_


