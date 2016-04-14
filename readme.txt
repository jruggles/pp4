pp4.py

---------------------------
Created by Jonathan Ruggles
Language: Python 2.7.10
Compiler Version: GCC 4.2.1
OS: Apple OS X 10.11.3
---------------------------

This program will take a matrix containing 10,000 float values, and it
will find the cube root of those values through three methods.
	- Newton's Method
	- Newton's Method which has been optimized for floating point values
	- Python's built in 'pow' function
It will time each function and save each of their results, which will then
be juxtaposed to determine their accuracy.

To run this program, compile and run it from the command line along with
a matrix file containing the input values and a file for output.
For example, from the command line in OS X it would look like this:

"$ python pp4.py inputFile.txt outputFile.txt"




SOURCES:

I relied on some of the methods provided in Ken Turkowski's "Finding the
Cube Root" to optimize my own method. This can be found here:

https://people.freebsd.org/~lstewart/references/apple_tr_kt32_cuberoot.pdf




PROGRAM OUTPUT:

Base Timing for System Overhead:
0.00277900695801

Built in power function best time:
0.0057590007782

Optimized Newton's Method best time:
0.046667098999

Brute Force Newton's Method best time:
1.15395998955

Norm-1 of Optimized Output - Built In Output:
1.01999830804e-09

Norm-1 of Brute Force Output - Built In Output:
1.03935349216e-09

Timing Ratio between Optimized / Built In:
14.7275782063

Timing Ratio between Brute Force / Built In:
386.303144252
