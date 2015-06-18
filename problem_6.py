# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares
# of the first ten natural numbers and the square
# of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

def main():
    first_100 = [i for i in range(1,101)]
    sum_of_squares = sum(map(lambda x: x**2,first_100))
    squared_sum = sum(first_100) ** 2

    print "The difference between the sum of squares of"
    print "the first 100 natural numbers and the square of the sum is:"
    print squared_sum - sum_of_squares


main()
