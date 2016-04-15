'''
pp4.py
Jonathan Ruggles
CS3513
'''

import numpy as np
from math import frexp, ldexp, pow
import sys
import time

def returnOne():
	'''
	Base function to determine system overhead
	'''
	return 1.0


def optRoot(x, nfraction):
	'''
	Optimied Newton's Method function
	'''
	e = sys.float_info.epsilon
	a, exp = frexp(x)
	shiftexp = exp%3
	if shiftexp > 0:
		shiftexp -= 3
	newexp = (exp - shiftexp) / 3
	a = ldexp(a, shiftexp)
	approx = a
	better = ((nfraction)*(((2.0)*approx)+((a)/(approx*approx))))

	while abs(better - approx) > e:
		approx = better
		better = ((nfraction)*(((2.0)*approx)+((a)/(approx*approx))))

	y = ldexp(approx, newexp)
	return y


def newtonRoot(x):
	'''
	Brute Force Newton's Method function
	'''
	e = sys.float_info.epsilon
	approx = x / 3.0
	better = ((1.0/3.0)*(((2.0)*approx)+((x)/(approx**(2)))))

	while abs(better - approx) > (1000 * e):
		approx = better
		better = ((1.0/3.0)*(((2.0)*approx)+((x)/(approx**(2)))))

	return approx


def builtIn(x):
	'''
	Python standard library cube root function
	'''
	return pow(x, (1.0/3.0))


if __name__ == "__main__":
	try:
		inA = sys.argv[1]
		outB = sys.argv[2]

	except IndexError:
		print "Insufficient parameters supplied."
		print "Usage: python pp4.py <input_file> <output_file>"
		sys.exit(1)

'''
Initialize the input and output data
'''
A = np.loadtxt(inA)
baseTiming = []
baseOutput = []
optimizedTiming = []
optimizedOutput = []
bruteForceTiming = []
bruteForceOutput = []
builtInTiming = []
builtInOutput = []
output = []
toggle = True
oneThird = (1.0/3.0)


'''
Each one of these blocks will run through a function 11 times.
The frist time will be to store the output in an array, and
the subsequent 10 will only calculate and return the values
(though they will not be stored anywhere). All iterations will
be timed and we will compare the best times of each.
'''

print "Base"
for _ in xrange(11):
	start = time.time()
	for x in A:
		cubeA = returnOne()
		if toggle:
			baseOutput.append(cubeA)
	stop = time.time()
	baseTiming.append(stop - start)
	toggle = False
baseTiming.sort()
print "Best time: ", baseTiming[0]
toggle = True

print "Optimized"
for _ in xrange(11):
	start = time.time()
	for x in A:
		cubeA = optRoot(x, oneThird)
		if toggle:
			optimizedOutput.append(cubeA)
	stop = time.time()
	optimizedTiming.append(stop - start)
	toggle = False
optimizedTiming.sort()
print "Best time: ", optimizedTiming[0]
toggle = True
optimizedArray = np.array(optimizedOutput)

print "Brute Force"
for _ in xrange(11):
	start = time.time()
	for x in A:
		cubeA = newtonRoot(x)
		if toggle:
			bruteForceOutput.append(cubeA)
	stop = time.time()
	bruteForceTiming.append(stop - start)
	toggle = False
bruteForceTiming.sort()
print "Best time: ", bruteForceTiming[0]
toggle = True
bruteForceArray = np.array(bruteForceOutput)

print "Built In"
for _ in xrange(11):
	start = time.time()
	for x in A:
		cubeA = builtIn(x)
		if toggle:
			builtInOutput.append(cubeA)
	stop = time.time()
	builtInTiming.append(stop - start)
	toggle = False
builtInTiming.sort()
print "Best time: ", builtInTiming[0]
builtInArray = np.array(builtInOutput)

ratioNM = (bruteForceTiming[0] - baseTiming[0]) / (builtInTiming[0] - baseTiming[0])
ratioOpt = (optimizedTiming[0] - baseTiming[0]) / (builtInTiming[0] - baseTiming[0])

bruteForceNorm = np.linalg.norm((bruteForceArray - builtInArray), 1)
optimizedNorm = np.linalg.norm((optimizedArray - builtInArray), 1)

output.append("Base Timing for System Overhead:")
output.append(baseTiming[0])
output.append("")
output.append("Built in power function best time:")
output.append(builtInTiming[0])
output.append("")
output.append("Optimized Newton's Method best time:")
output.append(optimizedTiming[0])
output.append("")
output.append("Brute Force Newton's Method best time:")
output.append(bruteForceTiming[0])
output.append("")
output.append("Norm-1 of Optimized Output - Built In Output:")
output.append(optimizedNorm)
output.append("")
output.append("Norm-1 of Brute Force Output - Built In Output:")
output.append(bruteForceNorm)
output.append("")
output.append("Timing Ratio between Optimized / Built In:")
output.append(ratioOpt)
output.append("")
output.append("Timing Ratio between Brute Force / Built In:")
output.append(ratioNM)

np.savetxt(outB, output, fmt="%s")
