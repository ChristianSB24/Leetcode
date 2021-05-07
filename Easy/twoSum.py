''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''

def twoSum(a, target):
    # Initialize a dictionary to store values.
    h = {}
    # Create dictionary from list. Want to create it before the loop so it is not recreated each cycle. 
    b = enumerate(a)
    # x gives key of dictionary, y gives value of dictionary
    for x, y in b:
        compliment = target - y
        # First want to check if compliment is in h. If it's not then y is set as key and x is set as value in h. Remember h is a dictionary. This gives {y: x}.
        # If compliment is in the keys of h then this means that we have found the two numbers that equal the target, compliment and y. 
        # Since we have created a dictionary we have access to the indices of the compliment and y. Return the index of compliment and return x. 
        if compliment not in h:
                h[y] = x
        else:
            return [h[compliment], x]

# Example
a = [3, 3]
target = 6
print(twoSum(a, target))


