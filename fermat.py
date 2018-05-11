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
"""


def prime_test(N, k):
    if is_carmichael(N):
        return 'carmichael'
    # Loop for as many times as k
    for x in range(0,k):
        # Pick some int 1 <= a <= N at random
        a = np.random.randint(1, N)
        # Apply Fermat's theorem to see if N is prime
        prime = False
        if mod_exp(a, N-1, N) == 1:
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
"""


def mod_exp(x, y, N):
    # base case
    if y == 0:
        return 1
    z = mod_exp(x, np.floor(y/2), N)
    if np.mod(y, 2) == 0:
        return np.mod(np.power(z, 2), N)
    else:
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
    # You will need to implement this function and change the return value.
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
    
"""


def is_carmichael(N):
    if N % 2 == 0:
        return False
    s = np.sqrt(N)
    factor_found = False
    a = 2
    while a < N:

        if a > s and not factor_found:
            return False
        if gcd(a, N) > 1:
            factor_found = True
        else:
            if mod_exp(a, N - 1, N) != 1:
                return False
        a += 1
    return True


def gcd(a,b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)
