import numpy as np

A=np.arange(9).reshape((3,3))
B=np.array([-1,2,0])

print (np.linalg.lstsq(A,B)[0])
