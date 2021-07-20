"""Faster than 92.19% of all Python solutions. Memory usage beats 82.19% of all solutions.
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


The main idea is that you want to get the string with the smallest amount of elements to avoid an index error 
and then cycle through each letter and see if the letters match in each word. If they do then add them to the answer. 
If they don't then don't include them. """
def com_pref(strs):
    answer = ''
    if len(strs) == 0: return ""
    a = min(strs, key=len)
    for i in range(len(a)):
        temp = False
        for word in strs:
            if a[i] == word[i]:
                temp = True
                continue
            else:
                temp = False
                break
        if temp == True:
            answer += a[i]
        else:
            break
    return answer

def comPref(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

