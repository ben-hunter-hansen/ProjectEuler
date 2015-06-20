# Project Euler Problem #9
# -----------------------------------------
# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.

from random import randint
from math import sqrt
from functools import reduce

# Generates a unique Pythagorean triplet
# based on a modified version of Euclid's formula described here:
# https://en.wikipedia.org/?title=Pythagorean_triple#Generating_a_triple
def gen_triplet(m,n,k):
    a, b, c = k*(m**2 - n**2), k*(2*m*n), k*(m**2 + n**2)
    return (a, b, c)

# Creates an argument list used for triplet generation
# @param limits     Maximum values for m,n and k
def arg_gen(limits):
    limit_mn, limit_k = limits
    rnd = lambda lim: randint(1,lim)
    m, n, k = rnd(limit_mn),rnd(limit_mn),rnd(limit_k)
    if m < n: m, n = n, m
    return (m,n,k)

# Attempts to locate a Pythagorean triplet where
# a + b + c = @param target
def triplet_with_sum(target):
    limit_mn = int(sqrt(target))
    limit_k = int(sqrt(limit_mn))
    for i in range((2*limit_mn)*limit_k):
        m, n, k = arg_gen((limit_mn,limit_k))
        triplet = gen_triplet(m,n,k)
        if sum(triplet) == target and not any(i == 0 for i in triplet):
            return triplet

    return triplet_with_sum(target)


def main():
    target = 1000
    abc = triplet_with_sum(target)
    product_abc = reduce(lambda x,y: x*y, abc)
    print "The product abc when a + b + c = %d is: %d" % (target,product_abc)

main()
