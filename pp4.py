'''
pp4.py
Jonathan Ruggles
CS3513
'''

import numpy as np
from math import frexp, ldexp, pow
import sys
import datetime

def returnOne():
	return 1.0


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


def newtonRoot(x):
	approx = (1.0/3.0) * x
	better = ((1.0/3.0)*(((2.0)*approx)+((x)/(approx**(2)))))

	while abs(better - approx) > 0.0000000000005:
		approx = better
		better = ((1.0/3.0)*(((2.0)*approx)+((x)/(approx**(2)))))

	return approx


def builtIn(x):
	return pow(x, (1.0/3.0))


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
A = np.loadtxt(inA)


print "Base"
for _ in xrange(10):
	start = datetime.datetime.now()
	for x in A:
		cubeA = returnOne()
	stop = datetime.datetime.now()
	print stop - start

print "Optimized"
for _ in xrange(10):
	start = datetime.datetime.now()
	for x in A:
		cubeA = optRoot(x)
	stop = datetime.datetime.now()
	print stop - start

print "Brute Force"
for _ in xrange(10):
	start = datetime.datetime.now()
	for x in A:
		cubeA = newtonRoot(x)
	stop = datetime.datetime.now()
	print stop - start

print "Built In"
for _ in xrange(10):
	start = datetime.datetime.now()
	for x in A:
		cubeA = builtIn(x)
	stop = datetime.datetime.now()
	print stop - start


#np.savetxt(outB, A, fmt="%f")
