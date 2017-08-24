def construct(pattern):
    next = [0] * (len(pattern))
    next[0] = -1
    next[1] = 0

    for i in range(2, len(pattern)):
        k = next[i - 1]
        while k > 0 and pattern[i - 1] != pattern[k]:
            k = next[k]

        if pattern[i - 1] == pattern[k]:
            k = k + 1

        next[i] = k

    return next

def construct2(pattern):
    next = [0] * (len(pattern))
    next[0] = -1

    i = 0
    k = -1
    while i < len(pattern)-1:
        if k == -1 or pattern[i] == pattern[k]:
            i += 1
            k += 1
            next[i] = k
        else:
            k = next[k]
    return next

def kmp(pattern, target):
    next = construct(pattern)

    i = 0
    j = 0
    while i < len(target) and j < len(pattern):
        if target[i] == pattern[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(pattern):
        return i - j
    else:
        return False


a = construct("ababaca")
b = construct2("ababaca")
print kmp("ababaca", "ababacbababacaababacc")