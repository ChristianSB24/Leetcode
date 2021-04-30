Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

def romVal(s):
    # We first create the dictionary with the roman values as keys and their values for easy reference to them. 
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #Initialize the current, previous, and total amount.
    curr = 0
    prev = 0
    total = 0
    for i in range(len(s)):
        # Using the for loop with the range allows us to get the element from the string starting from index 0 which is given as 
        # input to the dictionary. This then returns the value of that key/element.
        curr = values[s[i]]
        # In roman numerals the values go from largest to smallest. If the current value is greater than the previous one then we 
        # know the pattern is different. This pattern only changes if we have encountered a IV, IX, XL,... and so on.
        # Normally if you have XVI you just add them up (10 + 5 + 1 = 16). But if you have XIV and you try the same you end up with 
        # (10 + 1 + 5 = 16) or if you have CXL you have (100 + 10 + 50 = 160). This is of course wrong. But if you notice
        # you can see that the difference from the correct value is just 2*I or 2*X. You can use this pattern to create a 
        # simple solution to finding the roman numeral values. 
        if curr > prev:
            # This is only true if we have something like IV, IX, XL, XC, and so on.
            total = total + curr - 2*prev
        else:
            # This is the normal pattern such as III, VI, XV.
            total = total + curr
        # We set prev equal to curr to make sure we keep track of what came before for the future cycle.
        prev = curr
    return total 

print(romVal(s))



