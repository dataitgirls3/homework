#1
def add_1(x):
    return [i+1 for i in x]

print(add_1([1, 2, 3]))

#2
def square(x):
    return [i**2 for i in x]

print(square([1, 2, 3]))

#3
def filter_by_length(x, n):
    return [i for i in x if len(i) == n]

print(filter_by_length(['hi', 'mate'], 4))

#4
def without_vowels(x):
    vowels = ['a','i','u','e','o']
    return ''.join([x for x in x if x not in vowels])

print(without_vowels('dataitgirls3'))