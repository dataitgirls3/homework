import random

import pytest

random.seed(0)
list_length = (5, 25)
num_iter = 10


@pytest.fixture(scope='module')
def solution(request):
    githubid = request.config.getoption('githubid')
    solution_module = f'homework03_{githubid}'

    try:
        namespace = __import__(f'solutions.{solution_module}')
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')
    else:
        return getattr(namespace, solution_module)


def make(min_len, max_len):
    return random.sample(range(100), random.randint(min_len, max_len))

@pytest.mark.parametrize('price, quantity, answer', [
    ({'tuna can': 2000}, {'tuna can': 1}, 2000),
    (
        {'tuna can': 2000, 'sand': 10000, 'biscuit': 5000},
        {'tuna can': 10,'sand': 1,'biscuit': 2},
        40000
    ),
    ({}, {}, 0)
])
def test_problem10(price, quantity, answer, solution):
    assert answer == solution.net_order_value(price, quantity)


@pytest.mark.parametrize('x, y, answer', [
    ([1, 2], [1, 2], 0.25),
    ([1, 2], [-1, -2], -0.25)
])
def test_problem11(x, y, answer, solution):
    assert abs(answer - solution.covariance(x, y)) < 1e-8


@pytest.mark.parametrize('x, y, answer', [
    ([1, 2], [1, 2], 1),
    ([1, 2], [-1, -2], -1)
])
def test_problem12(x, y, answer, solution):
    assert abs(answer - solution.corrcoef(x, y)) < 1e-8


@pytest.mark.parametrize('x, answer', [
    ([1, 2, 3], True),
    ([1, 1, 1], True),
    ([1, 3, 2], False),
    ([3, 2, 1], False)
])
def test_problem13(x, answer, solution):
    assert answer == solution.ascending(x)