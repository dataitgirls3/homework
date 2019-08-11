import random

import pytest

random.seed(0)
list_length = (5, 25)
num_iter = 10


@pytest.fixture(scope='module')
def solution(request):
    githubid = request.config.getoption('githubid')
    solution_module = f'homework01_{githubid}'

    try:
        namespace = __import__(f'solutions.{solution_module}')
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')
    else:
        return getattr(namespace, solution_module)


def make(min_len, max_len):
    return random.sample(range(100), random.randint(min_len, max_len))


@pytest.mark.parametrize('_', range(10))
def test_problem1(_, solution):
    xs = make(*list_length)
    assert all([x+1 == y for x, y in zip(xs, solution.add_1(xs))])


@pytest.mark.parametrize('_', range(10))
def test_problem2(_, solution):
    xs = make(*list_length)
    assert all([x**2 == y for x, y in zip(xs, solution.square(xs))])


@pytest.mark.parametrize('x, n, answer', [
    (['hi', 'mate'], 4, ['mate']),
    (['hi', 'mate'], 2, ['hi']),
    (['hi', 'mate'], 1, []),
    (['americano', 'cafe latte', 'water'], 5, ['water'])
])
def test_problem3(x, n, answer, solution):
    assert answer == solution.filter_by_length(x, n)


@pytest.mark.parametrize('x, answer', [
    ('math', 'mth'),
    ('statistics', 'sttstcs'),
    ('ART', 'RT')
])
def test_problem4(x, answer, solution):
    assert answer == solution.without_vowels(x)