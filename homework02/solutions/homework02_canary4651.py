# 5
def variance(x):
    mean = sum(x)/len(x)
    return sum((i - mean)**2 for i in x)/len(x)

#6
import math

def stddev(x):
    return math.sqrt(variance(x))

#7  딕셔너리의 키와 값을 바꾸는 함수
def invert(x):
    return {v:k for k,v in x.items}

#8 : 두 리스트를 하나의 딕셔너리로 합쳐주는 함수
def to_dict(x, y):
    return {k:v for k,v in zip(x,y)}


#9

from collections import Counter

def mode(x):
    counter_x = Counter(x)
    return [i for i in counter_x if counter_x[i] == max(counter_x.values())]

