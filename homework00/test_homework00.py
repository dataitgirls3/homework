import random

import pytest

random.seed(0)
list_length = (5, 25)
num_iter = 10


@pytest.fixture(scope='module')
def solution(request):
    githubid = request.config.getoption('githubid')
    solution_module = f'homework00_{githubid}'

    try:
        namespace = __import__(f'solutions.{solution_module}')
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')
    else:
        return getattr(namespace, solution_module)


def make(min_len, max_len):
    return random.sample(range(100), random.randint(min_len, max_len))

@pytest.mark.parametrize('_', range(10))
def test_problem0_1(_, solution):
    xs = make(*list_length)
    assert all([x+1 == y for x, y in zip(xs, solution.add_1(xs))])


@pytest.mark.parametrize('_', range(10))
def test_problem0_2(_, solution):
    xs = make(*list_length)
    assert all([x**2 == y for x, y in zip(xs, solution.square(xs))])


@pytest.mark.parametrize('x, answer', [
    ([1, 2, 3, 4, 5], 11.0),
    ([2, 3, 4, 5], 13.5),
    ([1, 2, 3, 4], 7.5)
])
def test_problem0_3(x, answer, solution):
    assert abs(answer - solution.squared_mean(x)) < 1e-8