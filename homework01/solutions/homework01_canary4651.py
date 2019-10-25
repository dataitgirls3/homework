#1
def add_1(x):
    return [i+1 for i in x]


#2
def square(x):
    return [i**2 for i in x]


#3
def filter_by_length(x, n):
    return [i for i in x if len(i) == n]


#4
def without_vowels(x):
    vowels = 'aeiou'
    return ''.join([i for i in x if i.lower() not in vowels])