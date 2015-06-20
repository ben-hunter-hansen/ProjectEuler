# Project Euler Problem #7
# -----------------------------------------
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10,001st prime number?

import math
from euler.mathtools import Primes

# Sums up all prime indicies of a
# and adds their values to a list
def seive_to_dict(a):
    primes = {"total": sum(a), "values": []}
    for i in xrange(0,len(a)):
        if a[i] == True: primes["values"].append(i)
    return primes


def main():
    c = 150000 # 13,848 prime numbers appear before this constant
    prime_data = seive_to_dict(Primes.seive(c))
    primes = prime_data["values"]
    target_prime = primes[10001 - 1] # zero based
    print "The 10001th prime number is: %d" % target_prime


main()
