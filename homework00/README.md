# Comprehension
코드를 길게 작성해도 되지만, list 또는 dict comprehension으로 풀었을 때 한 줄로 해결할 수 있는 문제들입니다.

# Problem 0-1
정수 리스트가 주어졌을 때, 각 원소에 1씩 더한 새로운 리스트를 반환하는 함수를 작성하십시오.
```python
def add_1(x):
    pass
```
예를 들어,
```
>>> add_1([1, 2, 3])
[2, 3, 4]
```

# Problem 0-2
리스트가 주어졌을 때, 리스트 원소들의 제곱을 구하는 함수를 작성하십시오.
```python
def square(x):
    pass
```
예를 들어,
```
>>> square([1, 2, 3])
[1, 4, 9]
```

# Problem 0-3
리스트가 주어졌을 때, 리스트 원소들의 제곱의 평균을 구하는 함수를 작성하십시오.
```python
def squared_mean(x):
    pass
```
예를 들어,
```
>>> squared_mean([1, 2, 3, 4, 5])
11.0
>>> squared_mean([2, 3, 4, 5])
13.5
```

# 제출
과제 제출은 `solutions/homework00_(github 아이디).py`로 제출하시면 됩니다. 예를 들면 `homework00_ysunmi0427.py` 파일을 `solutions` 디렉토리에 넣으면 됩니다.

# 채점
로컬에서 채점을 해보기 위해서는 pytest가 필요합니다. `pip install pytest` 또는 `pip3 install pytest`로 설치해주세요.

설치 이후에는 다음과 같이 테스트 파일을 실행할 수 있습니다.
```
pytest -v test_homework00.py --githubid (GitHub 아이디)
```
예를 들어, 저는 터미널에서 아래를 실행 할 수 있습니다.
```
pytest -v test_homework00.py --githubid ysunmi0427
```