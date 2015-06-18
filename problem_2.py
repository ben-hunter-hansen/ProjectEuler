# Project Euler Problem #2
# -----------------------------------------
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.

def fib_even_values(a,b,evens):
    if b >= 4000000:
        return sum(evens)
    c = a + b
    if c % 2 == 0:
        evens.append(c)
    return fib_even_values(b,c,evens)


def main():
    total = fib_even_values(0,1,[])
    print "Sum of all even Fibonacci numbers < 4 million: %d" % total

main()
