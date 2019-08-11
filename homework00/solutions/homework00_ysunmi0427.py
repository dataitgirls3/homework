def add_1(x):
    return [i+1 for i in x]


def square(x):
    return [i**2 for i in x]


def squared_mean(x):
    return sum(square(x))/len(x)