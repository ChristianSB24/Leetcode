from collections import Counter

def anagram(s):
    if (len(s) % 2) != 0:
        return -1
    counter = 0
    a = s[:int(len(s)/2)]
    b = s[int(len(s)/2):]
    x = Counter(a)
    y = Counter(b)
    for i in list(set(a)):
        if (x[i] - y[i]) > 0:
            counter += (x[i] - y[i])
    return counter


