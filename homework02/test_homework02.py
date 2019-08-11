import random

import pytest

random.seed(0)
list_length = (5, 25)
num_iter = 10


@pytest.fixture(scope='module')
def solution(request):
    githubid = request.config.getoption('githubid')
    solution_module = f'homework02_{githubid}'

    try:
        namespace = __import__(f'solutions.{solution_module}')
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')
    else:
        return getattr(namespace, solution_module)


def make(min_len, max_len):
    return random.sample(range(100), random.randint(min_len, max_len))

@pytest.mark.parametrize('x, var', [
    ([1, 2, 3, 4, 5], 2.0),
    ([70, 80, 100, 120], 368.75),
    ([30, 30, 30], 0),
    ([-1, 1, -1, 1], 1)
])
def test_problem5(x, var, solution):
    assert abs(var - solution.variance(x)) < 1e-8


@pytest.mark.parametrize('x, std', [
    ([1, 2, 3, 4, 5, 6, 7], 2.0),
    ([1, -1], 1.0),
    ([0], 0.0)
])
def test_problem6(x, std, solution):
    assert abs(std - solution.stddev(x)) < 1e-8


@pytest.mark.parametrize('x, answer', [
    ({'cat':10, 'dog':20}, {10:'cat', 20:'dog'}),
    ({'lunch':25}, {25:'lunch'})
])
def test_problem7(x, answer, solution):
    assert answer == solution.invert(x)


@pytest.mark.parametrize('x, y, answer', [
    (['white cat', 'black cat'], [2, 3], {'white cat':2, 'black cat':3}),
    (['blue', 'red'], [10, 30], {'blue':10, 'red':30})
])
def test_problem8(x, y, answer, solution):
    assert answer == solution.to_dict(x, y)


@pytest.mark.parametrize('x, answer', [
    ([1, 2, 3, 3], [3]),
    ([1, 2, 3, 3, 4, 4], [3, 4])
])
def test_problem9(x, answer, solution):
    assert sorted(answer) == sorted(solution.mode(x))