def add_1(l):
    return [x + 1 for x in l]

def square(l):
    return [x ** 2 for x in l]

def filter_by_length(l, n):
    filtered = []
    for x in l:
        if len(x) == n:
            filtered.append(x)
    return filtered

def without_vowels(s):
    filtered_s = ''
    s_list = list(s)

    for x in s_list:
        if x not in 'aeiouAEIOU':
            filtered_s += x
    return filtered_s
