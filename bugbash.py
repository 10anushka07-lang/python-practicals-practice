
"""def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([10,20,30]))"""


"""def reverse_string(s):
    return s[::-1]

print(reverse_string("12345"))"""

"""def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'a': 1}
dict2 = {'b': 2}
print(dict1)
def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1 # just gave the dictionary used in the function the same name 

dict1 = {'a': 1}
dict2 = {'b': 2}
print(merge_dicts(dict1,dict2))
def merge_dicts(d1, d2):
	d1.update(d2)
	return d1
 
dict1 = {'a': 1}
dict2 = {'b': 2}
print(merge_dicts(dict1, dict2))
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count # did not return anything earlier 

c = Counter()
print(c.increment())  # Output expected: 1
print(c.increment())  # Output expected: 2"""
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print("factorial of 5:",factorial(5))
print("factorial of 8:",factorial(8))





