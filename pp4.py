'''
pp4.py
Jonathan Ruggles
CS3513
'''

import numpy as np
from math import frexp, ldexp, pow
import sys
import datetime


def optRoot(x):
	e = sys.float_info.epsilon
	y = x
	a, exp = frexp(y)
	nfraction = 1.0/3.0
	iteration = 0
	shiftexp = exp%3
	if shiftexp > 0:
		shiftexp -= 3
	nexp = (exp - shiftexp) / 3
	a = ldexp(a, shiftexp)
	approx = nfraction * a
	better = ((nfraction)*(((2.0)*approx)+((a)/(approx*approx))))

	while abs(better - approx) > e:
		approx = better
		better = ((nfraction)*(((2.0)*approx)+((a)/(approx*approx))))
		iteration += 1

	y = ldexp(approx, nexp)
	return y


def newtonRoot(x, n):
	nfraction = 1.0/n
	nminus = n-1
	approx = nfraction * x
	better = ((nfraction)*(((nminus)*approx)+((x)/(approx**(nminus)))))

	while abs(better - approx) > 0.0000000000005:
		approx = better
		better = ((nfraction)*(((nminus)*approx)+((x)/(approx**(nminus)))))

	return approx


if __name__ == "__main__":
	try:
		inA = sys.argv[1]
		outB = sys.argv[2]

	except IndexError:
		print "Insufficient parameters supplied."
		#sys.exit(1)

'''
Initialize the input and output data
'''
M = np.matrix(np.loadtxt(inA))
A = np.squeeze(np.asarray(M))
print A

#X = np.random.uniform(1000000, 100000000, 10000)

print "Optimized"
print datetime.datetime.now()

for x in A:
	cubeA = optRoot(x)

print datetime.datetime.now()

print "Brute Force"
print datetime.datetime.now()

for x in A:
	cubeA = newtonRoot(x, 3.0)


print datetime.datetime.now()

print "Built In"
print datetime.datetime.now()

for x in A:
	cubeA = pow(x, (1.0/3.0))

print datetime.datetime.now()


#np.savetxt(outB, X, fmt="%f")
