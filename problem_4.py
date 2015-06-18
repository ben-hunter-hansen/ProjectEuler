# Project Euler Problem #4
# -----------------------------------------
# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    list_digits = lambda num: map(int, str(num))
    digits = list_digits(n)

    def split_list(list,modifier=0):
        left = list[:(len(list)-modifier)/2]
        right = list[(len(list)+modifier)/2:]
        return (left, right)

    if len(digits) % 2 == 0:
        left_side,right_side = split_list(digits)
        return left_side == list(reversed(right_side))
    else:
        left_side,right_side = split_list(digits,1)
        return left_side == list(reversed(right_side))

def largest_palindrome(min,max):
    largest_pal = 0
    for i in reversed(xrange(min,max)):
        for j in reversed(xrange(min,max)):
            product = i * j
            if is_palindrome(product):
                if product > largest_pal:
                    largest_pal = product
    return largest_pal


def main():
    print "The largest palindrome that is a product of 3 digit numbers is: %d" % largest_palindrome(100,999)

main()
