# Comprehension
코드를 길게 작성해도 되지만, list 또는 dict comprehension으로 풀었을 때 한 줄로 해결할 수 있는 문제들입니다.

# Problem 5
정수 리스트를 받아 분산을 계산하는 함수를 작성하세요. 분산은 편차의 제곱의 평균입니다. 파이썬 내장함수만 사용하세요.
```python
def variance(x):
    pass
```

# Problem 6
정수 리스트를 받아 표준편차를 계산하는 함수를 작성하세요. 표준편차는 분산의 제곱근입니다. 파이썬 내장함수만 사용하세요.
```python
import math

def stddev(x):
    pass
```

# Problem 7
딕셔너리의 키와 값을 바꾸는 함수를 작성하십시오. 같은 값을 가지는 키는 없다고 가정합시다. (키와 값은 1:1 관계입니다.)
```python
def invert(x):
    pass
```
예상되는 결과는,
```
>>> cute_rating = {'cat':10, 'human':2, 'whale':100}
>>> invert(cute_rating)
{10:'cat', 2:'human', 100:'whale'}
```

# Problem 8
두 리스트를 하나의 딕셔너리로 합쳐주는 함수를 작성해주세요.
```python
def to_dict(x, y):
    pass
```

```
>>> to_dict(['white cat', 'black cat', 'cheese cat'], [2, 3, 7])
{'white cat':2, 'black cat':3, 'cheese cat':7}
```

# Problem 9
정수 리스트를 받아 최빈값이 들어있는 새로운 리스트를 돌려주는 함수를 작성하세요. 
```python
from collections import Counter

def mode(x):
    pass
```
```
>>> mode([1, 2, 3, 3])
[3]
>>> mode([1, 2, 3, 3, 4, 4])
[3, 4]
```

# 제출
과제 제출은 `solutions/homework02_(github 아이디).py`로 제출하시면 됩니다. 예를 들면 `homework02_ysunmi0427.py` 파일을 `solutions` 디렉토리에 넣으면 됩니다.

# 채점
다음과 같이 테스트 파일을 실행할 수 있습니다.
```
pytest -v test_homework02.py --githubid (GitHub 아이디)
```
예를 들어, 저는 터미널에서 아래를 실행 할 수 있습니다.
```
pytest -v test_homework02.py --githubid ysunmi0427
```