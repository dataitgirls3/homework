# 10 : 상품의 가격과 구매수량이 주어졌을 때, 총 주문액수를 계산하는 함수를 작성하세요

def net_order_value(price, quantity):
    # total = 0
    # for i in price:
    #     total += price[i] * quantity[i]
    return sum([price[i] * quantity[i] for i in price])

# 11 : 두 정수 리스트가 주어졌을 떄, 공분산을 계산하는 함수 구현

def covariance(X, Y):
    avg = lambda n: sum(n)/len(n)
    ax, ay = avg(X), avg(Y)
    return sum((ax-x)*(ay-y) for x,y in zip(X,Y))/len(X)


# 12 : 두 정수 리스트가 주어졌을 때, 상관계수를 계산하는 함수 구현
# 상관관계는 공분산을 X, Y 각각의 표준편차를 나눠 계산
import numpy as np

def corrcoef(x, y):
    def stddev(n):
        avg = sum(n)/len(n)
        return np.sqrt(sum((i-avg)**2 for i in n)/len(n))
    return covariance(X,Y)/ (stddev(x)*stddev(y))

# 13 : 정수 리스트가 주어졌을 때, 이 리스트가 오름차순인지 확인하세요.
# 오름차순이라면 True를, 그렇지 않다면 False를 반환하는 함수를 작성하세요.

def ascending(x):
    return x==sorted(x)

# print(ascending([1, 2, 2]))
# print(ascending([2, 1, 3]))