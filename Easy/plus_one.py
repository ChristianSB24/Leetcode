""" Faster than 63% of all Python submissions. Uses less memory than 91.24% of all Python submissions.
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
    and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself. """

def plusOne(digits):
    number = ''
    answer = []
    for x in digits:
        number = number + str(x)
    number = int(number) + 1
    for i in str(number):
        answer.append(i)
    return answer
