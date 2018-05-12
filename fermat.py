import random
import numpy as np
"""
Description
-----------
Determine if a given number is prime, composite, or carmichael.

Parameters
----------
N : int
    N > 0. The number that we are trying to determine whether it is prime or composite or carmichael
k : int
    k > 0. The number of times we will run Femat's algorithm and will determine the accuracy of our primality assessment

Returns
-------
str
    The output should be a string that classifies N as 'prime', 'composite', or 'carmichael'
    
Problem Formulation
-------------------
Return ‘prime’ if N is a prime number, return 'carmichael' if N is a carmichael number, and return ‘composite’ otherwise

Complexity
----------
Because the for loop runs k times and if we assume that multiplication is the elementary operation
The mod_exp is N^2*log(N) with respect to multiplication being a N^2 operation
This function is called k times so k*N^2*log(N)
We should also add in the time to run the carmichael test
So k*N^2*log(N) + N^3*log(N)
Simplifies to N^3*log(N) if k is much less than N
"""


def prime_test(N, k):
    if is_carmichael(N):    # N^3*log(N) time complexity, only runs once
        return 'carmichael'
    # Loop for as many times as k
    for x in range(0, k):   # runs k times
        # Pick some int 1 <= a <= N at random
        a = np.random.randint(1, N) # Assume constant time
        # Apply Fermat's theorem to see if N is prime
        prime = False
        if mod_exp(a, N-1, N) == 1: # N^2*log(N)
            prime = True
        else:
            prime = False

        if not prime:
            return 'composite'
    return 'prime'

"""
Description
-----------
Perform the modulus operation on an exponential

Parameters
----------
x : int
    The number that has the exponent
y : int
    y >= 0. The exponent.
N : int 
    The second number in the modulus function
    
Returns
-------
int
    The output is the calculation of x^y mod N
    
Problem Formulation
-------------------
Given integers x, y, N
Find integer r = x^y mod N

Complexity
----------
We perform a multiply about log2(N) times and y is N - 1 so about N/2 which simplifies to N
Since multiplying is an N^2 operation we have N^2*log2(N) 
Assume that squaring is constant time

The space complexity will be 2N at the worst moment then the mod will bring it back to N bits
"""


def mod_exp(x, y, N):
    # base case
    if y == 0:
        return 1
    # Divide exponent by 2 and round down
    z = mod_exp(x, np.floor(y/2), N)    # Division by 2 y/2 times
    if np.mod(y, 2) == 0:
        # Power doubles the number of bits
        # Mod returns it to the same number of bits as N
        # Assume mod is an elementary operation
        return np.mod(np.power(z, 2), N)
    else:
        # Same as in if but there is an added multiply which is O(n^2)
        return np.mod(x*np.power(z, 2), N)
    return 1

"""
Description
-----------
Determine the probability that the assessment of a number N being prime is correct

Parameters
----------
k : int
    k > 0. The number of times we will run Femat's algorithm and will determine the accuracy of our primality assessment
    
Returns 
-------
float
    Return the percentage value of the probability that the assessment of a number N being prime is correct
    
Problem Formulation
-------------------
Given an integer k
Find a float (1 - 1/2^k)*100
"""

def probability(k):
    # Returns probability as a percentage
    # Squaring 2 is constant time in binary
    return (1-1/(np.power(2, k)))*100

"""
Description
-----------
Determine if a given number is a carmichael number

Parameters
----------
N : int
    N > 0. The number that we are trying to determine whether it is a carmichael number
a : int
    A number which is co-prime to N. The GCD of N and a is 1.
    
Returns
-------
boolean
    Return whether the number is a carmichael number or not

Problem Formulation
-------------------
Given two integers N and a
return True if N is a carmichael number otherwise return false
    
Complexity
----------
In the worst case the while loop runs N times
The mod_exp function runs every one of those times
so the time complexity is N^3*log(N)

The space complexity driven by mod_exp so 2*N bits
"""


def is_carmichael(N):
    # Check if N is even
    if N % 2 == 0:
        return False
    # Keep square root of N
    s = np.sqrt(N)
    # Constant to tell if a factor of N has been been found
    factor_found = False
    a = 2
    # a increments up to the value of N
    while a < N:    # Repeated N times
        # Check if N is composite
        if a > s and not factor_found:
            return False
        # See if a is coprime to N
        if gcd(a, N) > 1:   # gcd is log(n) time complexity
            factor_found = True
        # See if a is a factor of N
        else:
            if mod_exp(a, N - 1, N) != 1:   # N^2*log(N) time complexity
                return False
        # Increment a
        a += 1
    # If function gets to this point then N is a carmichael number
    return True

# Returns the greatest common divisor of integers a and b
# This function is log(n)^2 time complexity
# The space complexity is max(a, b)
def gcd(a,b):
    # Check to make sure a is larger than b
    if a < b:
        return gcd(b, a)
    # Base case
    if a % b == 0: # mod takes log(n) time complexity to compute
        return b
    # Recurse down
    return gcd(b, a % b)
