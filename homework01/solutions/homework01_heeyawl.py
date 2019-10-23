def add_1(x):
	return [i+1 for i in x]

def square(x):
	return [i ** 2 for i in x]

def filter_by_length(x,n):
	return [i for i in x if len(i) == n]

def without_vowels(x):
	vowels = ['a', 'e', 'i', 'o', 'u']
	split = [i for i in list(x) if i not in vowels]
	return ''.join(split) 
