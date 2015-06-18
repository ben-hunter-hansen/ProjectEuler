# Project Euler Problem #5
# -----------------------------------------
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

from functools import reduce

def divide_evenly_from(n,min,max):
    if max == min:
        return n
    if n % max == 0:
        return divide_evenly_from(n,min,max-1)

def main():
    all_nums = [i for i in range(1,21)]
    product = reduce(lambda a,b: a * b, all_nums)
    for i in xrange(1,product):
        found_smallest = divide_evenly_from(i,1,20)
        if found_smallest:
            print "smallest positive number divisible by all numbers 1-20 is:"
            print i
            break
main()
