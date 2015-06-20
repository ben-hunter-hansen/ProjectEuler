import math

class Primes:
    
    @staticmethod
    def seive(n):
        a = [True if i > 1 else False for i in range(n)]
        sqrt_real = lambda x: math.trunc(math.sqrt(x))+1
        for i in xrange(2,sqrt_real(n)):
            j, steps = i**2,1
            while j < len(a):
                a[j] = False
                j, steps = (i**2)+(steps*i), steps + 1
        return a
