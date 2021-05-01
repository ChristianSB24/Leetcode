Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:  -2**31 <= x <= 2**31 - 1

def reverse(n):
    # Stringify integer so we can access elements of it.
    a = str(n)
    # We want to check if it is negative first.
    if a[0] == '-':
        # If it is then get the number without the negative sign, then reverse the string, 
        # then slap on the negative sign onto the reversed string.
        a = a[1:]
        z = '-' + a[::-1]
    else:
        # Otherwise just give the returned string.
        z = a[::-1]
    # We want to check if it satisfies the constraint. If it doesn't then return 0.
    if int(z) >= 2**31-1 or int(z) <= -2**31: return 0
    return int(z)