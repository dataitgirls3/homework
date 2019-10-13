

homework01_heeyawl

def add_1(x):
    return [i+1 for i in x]

assert add_1([1, 2, 3]) == [2, 3, 4]

def square(x):
    return [i ** 2 for i in x]

assert square([1, 2, 3]) == [1, 4, 9]

def filter_by_length(x,n):
    return [i for i in x if len(i) == n]

assert filter_by_length(['hi', 'mate'], 4) == ['mate']
assert filter_by_length(['hi', 'mate'], 1) == []

