"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


For this problem I gave two solutions. 

In this first solution I use mathematics to reverse the string. """
def palNum(x):
    # We first initialize the reverse number variable and make a copy of the input. 
    revs_number = 0
    a = x
    # Next we set up a while loop because we will be decreasing x until it is 0.
    while (x > 0):
        # % gives us the remainder. In this case if we divide by 10 the remainder will be the ones spot. 
        remainder = x % 10
        # Here we multiply the previous value of revs_number by 10. This makes more sense as you continue with the loop. 
        # Then add the remainder.
        revs_number = (revs_number * 10) + remainder
        # We now want the next digit of x. The // operator rounds the integer down to the nearest whole number after division. 
        # For example: 121 // 10 = 12.
        x = x // 10
    # Finally we check if the original input is equal to the reversed integer.
    return revs_number == a

"""This second solution is very simple. 
Turn the integer into a string and then check if the string is the same when its elements are reversed.
The a[::-1] has the syntax "list[<start>:<stop>:<step>]". 
So, when you do a[::-1], it starts from the end towards the first taking each element. So it reverses a. """
def palN(x):
    a = str(x)
    return a == a[::-1]




