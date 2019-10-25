def variance(x):
    m = sum(x) / len(x)
    diff = [(i - m) ** 2 for i in x]
    return sum(diff) / len(diff)

assert variance([1,2,3,4,5]) == 2

import math

def stddev(x):
    return math.sqrt(variance(x))

assert stddev([1,2,3,4,5]) == 2 ** 0.5

def invert(x):
    return {b:a for a,b in x.items()}

cute_rating = {'cat':10, 'human':2, 'whale':100}
assert invert(cute_rating) == {10:'cat', 2:'human', 100:'whale'}

def to_dict(x, y):
    return dict(zip(x,y))

assert to_dict(['white cat', 'black cat', 'cheese cat'], [2, 3, 7]) == {'white cat':2, 'black cat':3, 'cheese cat':7}

from collections import Counter
def mode(x):
    max_val = Counter(x).most_common()[0][1]
    l = [m for m, frequency in Counter(x).items() if frequency == max_val]
    return l

assert mode([1, 2, 3, 3]) == [3]
assert mode([1, 2, 3, 3, 4, 4]) == [3, 4]