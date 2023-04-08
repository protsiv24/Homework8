def mane_function(s):
    s2 = ''
    i = len(s) - 1
    while i >= 0:
        s2 = s2 + s[i]
        i = i - 1
        return s2
    s1 = "qwerty"
    s2 = mane_function(s1)  # s2 = 'ytrewq'