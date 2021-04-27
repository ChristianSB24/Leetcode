a = [3, 3]
# print(enumerate(a))
# for i, num in enumerate(a):
#     print(i)
#     print(num)
def twoSum(a, target):
    h = {}
    b = enumerate(a)
    for x, y in b:
        compliment = target - y
        if compliment not in h:
                h[y] = x
        else:
            return [h[compliment], x]

print(twoSum(a, 6))

# a = [2, 7, 11, 15]

# b = {k: v for v, k in enumerate(a)}

# b = dict(enumerate(a))

# print(b)

# print(b.keys())
# print(list(b.keys()))
# print(b.values())
# print(b.items())
# for x, y in b.items():
#   print(x, y)

# for x in b:
#     print(x)
# for x in b:
#     print(b[x])
