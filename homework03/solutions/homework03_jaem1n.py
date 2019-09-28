def net_order_value(price, quantity):
    return sum([price[i] * quantity[i] for i in price])

def covariance(x, y):
    def avg(z):
        return sum(z) / len(z)
    return sum([(i-avg(x)) * (j-avg(y)) for i,j in zip(x,y)]) / len(x)

import math

def corrcoef(x, y):
    def stddev(z):
        avg = sum(z) / len(z)
        return math.sqrt(sum((i - avg) ** 2 for i in z) / len(z))
    return covariance(x, y) / (stddev(x) * stddev(y))

def ascending(x):
    return x == sorted(x)