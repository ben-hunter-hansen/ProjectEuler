import math

# Find all prime numbers that appear before n
# @param n      Upper limit
# @return       List of all primes < n
def primes_under(n):

    # Seive of Eratosthenes implementation, algorithm found here:
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
    def seive(n):
        a = [True if i > 1 else False for i in range(n)]
        sqrt_real = lambda x: math.trunc(math.sqrt(x))+1
        for i in xrange(2,sqrt_real(n)):
            j, steps = i**2,1
            while j < len(a):
                a[j] = False
                j, steps = (i**2)+(steps*i), steps + 1
        return a

    a, primes = seive(n), []
    for i in xrange(0,len(a)):
        if a[i] == True: primes.append(i)

    return primes
