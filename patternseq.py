import numpy as np
from numba import njit

@njit
def give_seq_pattern(array):
	"""If it finds an uninterrupted repetition in the array, 
	returns the lenght of the partern of repetition
	else it returns a 0"""
	pastflag = False
	flag = False
	loc_flag = 0
	loc_plus = 0
	lenght = len(array)
	for i in range(1,lenght):
		flag = array[i] == array[loc_plus]
		#print('comparison ',array[i],array[loc_plus],flag)
		if flag and not pastflag:
			loc_flag = i
		if flag:
			loc_plus += 1
		elif not flag and pastflag:
			loc_flag = 0
			loc_plus = 0
		pastflag = flag
		#print('locs ',loc_flag,loc_plus)
	return loc_flag
#if __name__  == '__main__':
#a = np.array([0,0,1,0,2,0,3,0,4,0,0,1,0,2,0,3,0,4,0])
b = np.array([0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5])
#c = np.array([1,3,2,4,3,6,2,2,5,8,4,6,7,9,1,0,5,5])
give_seq_pattern(b)
# Con @njit esto se tarda 2.86666 segundos en analizar
# un array de 1024,000,000 de floats (en esta computadora :v)