# Project Euler Problem #3
# -----------------------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# TODO: This alg is taken from StackOverflow, mine was too
# slow and shitty.
def largest_prime_factor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

def main():
    n = 600851475143
    print "The largest prime factor of %d is %d" % (n, largest_prime_factor(n))
main()
