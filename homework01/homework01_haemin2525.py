#!/usr/bin/env python
# coding: utf-8

# # Problem 0-1
# 정수 리스트가 주어졌을 때, 각 원소에 1씩 더한 새로운 리스트를 반환하는 함수를 작성하십시오.
# 

# ```python
# def add_1(x):
#     pass
# ```
# 예를 들어,
# ```
# >>> add_1([1, 2, 3])
# [2, 3, 4]
# ```

# In[4]:


def add_1(a):
    a = [i + 1 for i in a]
    return a


# # Problem 0-3
# 리스트가 주어졌을 때, 리스트 원소들의 제곱의 평균을 구하는 함수를 작성하십시오.
# ```python
# def squared_mean(x):
#     pass
# ```
# 예를 들어,
# ```
# >>> squared_mean([1, 2, 3, 4, 5])
# 11.0
# >>> squared_mean([2, 3, 4, 5])
# 13.5
# ```

# In[2]:


import numpy as np


# In[3]:


def squared_mean(x):
    return np.mean([(i**2) for i in x])


# # Problem 4
# 단어에서 모음을 제거하는 함수를 만드세요.
# ```python
# def without_vowels(x):
#     pass
# 예를 들어,
# 
# >>> without_vowels('dataitgirls3')
# 'dttgrls3'
# >>> without_vowels('DATAITGIRLS3')
# 'DTTGRLS3'
# ```

# In[5]:


def without_vowels(x):
    v = ['a','e','i','o','u']
    x = x.lower()
    for i in x:
        if i in v:
            x = x.replace(i, "")  
    return x


# In[6]:


without_vowels('dataitgirls3')


# In[16]:


# 모음 없애기는 comprehension으로 어떻게 해야 할 지 모르겠습니다


# In[12]:


def without_vowels(x):
    v = "aeiouAEIOU"
    return x.replace(char,"") for char in v


# In[13]:


def without_vowels2(x):
    v = ["aeiouAEIOU"]
    for char in v:
        x = x.replace(char,"")
    return x


# In[14]:


without_vowels2('dataitgirls3')


# In[15]:


def without_vowels3(x):
    v = "aeiouAEIOU"
    for char in v:
        x = x.replace(char,"")
    return x


# In[11]:


without_vowels3('dataitgirls3')

