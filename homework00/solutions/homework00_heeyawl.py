## Problem 0-1

def add_1(x):
    return [i+1 for i in x]

assert add_1([1, 2, 3]) == [2, 3, 4]

## Problem 0-2

def square(x):
    return [i ** 2 for i in x]

assert square([1,2,3]) == [1,4,9]

## Problem 0-3
def squared_mean(x):
    return sum(square(x))/len(x)

assert squared_mean( [1, 2, 3, 4, 5]) == 11
assert squared_mean( [2, 3, 4, 5]) == 13.5
