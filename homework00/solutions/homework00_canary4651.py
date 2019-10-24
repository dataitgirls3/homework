def add_1(x):
    return [i+1 for i in x]

print(add_1([1, 2, 3]))

def square(x):
    return [i**2 for i in x]

print(square([1, 2, 3]))

def squared_mean(x):
    return sum(square(x))/len(x)

print(squared_mean([1, 2, 3, 4, 5]))


