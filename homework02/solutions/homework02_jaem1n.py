def variance(x):
    avg = sum(x) / len(x)
    return sum((i - avg) ** 2 for i in x) / len(x)

import math

def stddev(x):
    return math.sqrt(variance(x))

def invert(x):
    return {v:k for k, v in x.items()}

def to_dict(x, y):
    return {k:v for k, v in zip(x,y)}

from collections import Counter

def mode(x):
    cnt = Counter(x)
    return [i for i in cnt if cnt[i] == max(cnt.values())]