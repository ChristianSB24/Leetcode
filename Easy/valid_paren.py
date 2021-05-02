""" Faster than 98.94% of all Python solutions. Memory usage beats 99.70% of all solutions.
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order."""

def paren(s):
    # The main objective is to see if every open paren has a closing paren and is in the right order. 
    # For example if we have "{()}" we will cycle through each element and for a open paren we will add a closing paren to a list.
    # In this solution this list is must. So for the first paren must will be appended a "}".
    # The next element will append a ")". After that all we have are closing paren.
    # For each closing paren, if they match the last element of the list must (The corresponding closing paren for the most recent open paren).
    # Then that element is removed from the list. If the input is valid then this should occur for each closing paren.
    # Eventually len(must) == 0 and a True is returned. 
    must = []    
    close = [']',')','}']
    # We first check if the first element of the input is a closing paren. If this is true then the input is not valid.
    # I did this to increase the speed of the solution.
    if s[0] in close:
        return False
    # Similarly, check if the last element is an open paren. If true this means the input is not valid.
    if s[-1] not in close:
        return False
    for i in s:
        if i in close:
            # If must is not empty empty and i is equal to the last element of must then remove that element. Otherwise return False.
            if len(must) != 0:
                if i == must[-1]:
                    must.pop()
                else:
                    return False
            else:
                return False
        # If i is an opening paren then add the corresponding closing paren to the must list. 
        elif i == '{':
            must.append('}')
        elif i == '[':
            must.append(']')
        elif i == '(':
            must.append(')')
    # If all elements of must are gone then return True. Otherwise, return False.
    if len(must)==0:
        return True
    else:
        return False
