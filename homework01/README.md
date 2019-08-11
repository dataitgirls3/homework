# Comprehension
코드를 길게 작성해도 되지만, list 또는 dict comprehension으로 풀었을 때 한 줄로 해결할 수 있는 문제들입니다.

# Problem 1
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

# Problem 2
정수 리스트가 주어졌을 때, 각 원소의 제곱을 가지는 새로운 리스트를 반환하는 함수를 작성하십시오.
```python
def square(x):
    pass
```
예를 들어,
```
>>> square([1, 2, 3])
[1, 4, 9]
```

# Problem 3
문자열 리스트가 주어졌을 때, 특정 길이의 원소만을 가지는 새로운 리스트를 반환하는 함수를 작성하십시오.
```python
def filter_by_length(x, n):
    pass
```
예를 들어,
```
>>> filter_by_length(['hi', 'mate'], 4)
['mate']
>>> filter_by_length(['hi', 'mate'], 1)
[]
```

# Problem 4
단어에서 모음을 제거하는 함수를 만드세요.
```python
def without_vowels(x):
    pass
```
예를 들어,
```
>>> without_vowels('dataitgirls3')
'dttgrls3'
>>> without_vowels('DATAITGIRLS3')
'DTTGRLS3'
```

# 제출
과제 제출은 `solutions/homework01_(github 아이디).py`로 제출하시면 됩니다. 예를 들면 `homework01_ysunmi0427.py` 파일을 `solutions` 디렉토리에 넣으면 됩니다.

# 채점
다음과 같이 테스트 파일을 실행할 수 있습니다.
```
pytest -v test_homework01.py --githubid (GitHub 아이디)
```
예를 들어, 저는 터미널에서 아래를 실행 할 수 있습니다.
```
pytest -v test_homework01.py --githubid ysunmi0427
```

