# Project Euler Problem #8
# -----------------------------------------
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from euler.mathtools import Primes

def main():
    psum = sum(Primes.all_until(2000000))
    print "The sum of all primes below 2,000,000 is: %d" % psum

main()
