""" Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
    If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only. """

# def lenWord(s):
#     length = 0
#     prev = False
#     for i in range(len(s)):
#         if s[-1 - i] != ' ':
#             prev = True
#             length += 1
#         if s[-1 - i] == ' ' and prev == True:
#             return length
#         if s[-1 - i] == ' ':
#             continue
#     return length 

# def lenWord(s):
#     length = []
#     prev = False
#     s = s[::-1]
#     for i in range(len(s)):
#         if s[i] != ' ':
#             length.append(s[i])
#             prev = True
#         if s[i] == ' ' and prev == True:
#             break
#     return len(length)

# def lenWord(s):
#     s_list = s.strip().split(" ")
#     print(s_list)
#     l = len(s_list[len(s_list)-1])
#     return l
        
        
