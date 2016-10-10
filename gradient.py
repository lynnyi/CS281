
import numpy as np
import io


x = np.loadtxt('./RegressionData/Xmatrix.dat')
y = np.loadtxt('./RegressionData/yvector.dat')

n= len(y)
d = len(x[0])
alpha = .5
x_transpose = np.transpose(x)
beta = np.random.rand(d,1)/10
for i in range(1,100):
	grad = 1./n * np.dot(x_transpose, np.dot(x, beta) - y)
	if len(grad) is not d:
		print('error')
	#norm = np.linalg.norm(grad)
	#grad = grad / norm
	beta = beta - grad*alpha
	print np.linalg.norm(y - np.dot(x, beta))
	

