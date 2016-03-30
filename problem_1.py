# Project Euler Problem #1
# -----------------------------------------
# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# 

def get_multiples_of(n1,n2,limit):
    multiples = []
    for i in range(0,limit):
        if i % n1 == 0 or i % n2 == 0:
            multiples.append(i)
    return multiples


def main():
    sums = sum(get_multiples_of(3,5,1000))
    print "The sum of all multiples of 3 or 5 below 1000 is: %d" % sums


main()
