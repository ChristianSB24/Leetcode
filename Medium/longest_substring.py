"""Given a string s, find the length of the longest substring without repeating characters. """

def longSub(s):
    dic = {}
    res, last_match = 0, -1
    for i, c in enumerate(s):
        if c in dic and last_match < dic[c]:
            last_match = dic[c]
        res = max(res, i - last_match)
        dic[c] = i
    return res

