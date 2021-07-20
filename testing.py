# def withAnagrams(text):
#     duplicates = []
#     for x in text:
#         if sorted(x) not in duplicates:
#             print(sorted(x))
#             duplicates.append(sorted(x))
#         else:
#             text.remove(x)
#     return text

# def withAnagrams(text):
#     duplicates = []
#     for x in text:
#         if sorted(x) not in duplicates:
#             print(sorted(x))
#             duplicates.append(sorted(x))
#         else:
#             text.remove(x)
#     return text

# text = ['code', 'aaagmnrs', 'anagrams', 'doce']

# for x in range(10):
#     if x == 2:
#         x = (x * 2)
#     print(x)

# print(withAnagrams(text))

# print(text[2])

import math

# def pthFactor(n, p):
#     factorList = []
#     counter = 1
#     while (counter) <= n:
#         if (n % counter) == 0:
#             factorList.append(counter)
#             counter = counter*2
#             if len(factorList) >= p:
#                 print(factorList)
#                 return factorList[p-1]
#             continue   
#         counter += 1
#     if len(factorList) < p:
#         return 0
#     else:
#         print(factorList)
#         return factorList[p-1]

def pthFactor(n, p):
    factorList = []
    counter = 1
    # factorList.append(n)
    while counter*counter <= n:
        if (n % counter) == 0:
            factorList.append(counter)
            if (n//counter) != counter:
                factorList.append(n//counter)
        counter += 1
    sortedList = sorted(factorList)
    print(sortedList)
    if len(sortedList) < p:
        return 0
    else:
        return sortedList[p-1]

n = 1000
p = 5
print(pthFactor(n, p))