'''#Task 2 (Write a Python script to add a key to a dictionary.)
d = {0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d)'''
'''#Task 5 (Write a Python program to iterate over dictionaries using for loops.)
d = {'x': 1, 'y': 2, 'z': 3} 
for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)'''
'''#Task 8 (Write a Python script to merge two Python dictionaries.)
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)'''
'''#Task 9 (Write a Python program to iterate over dictionaries using for loops.)
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
    print(color_key, 'corresponds to ', d[color_key])'''
'''#Task 10 (Write a  Python program to sum all the items in a dictionary.)
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = sum(my_dict.values())
print(result)'''
'''#Task 11 (Write a Python program to multiply all the items in a dictionary.)
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1
for key in my_dict:
    result = result * my_dict[key]
print(result)'''
'''#Task 13 (Write a Python program to map two lists into a dictionary.)
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)'''
'''#Task 14 (Write a Python program to sort a given dictionary by key)
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))'''
'''#Task 15 (Write a Python program to get the maximum and minimum values of a dictionary.)
my_dict = {'x': 500, 'y': 5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])'''
'''#Task 18 (Write a Python program to check if a dictionary is empty or not.)
my_dict = {}
if not bool(my_dict):
    print("Dictionary is empty")'''
'''#Task 19 (Write a Python program to combine two dictionary by adding values for common keys.)
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)'''
'''#Task 21 (Write a Python program to create and display all combinations of letters, selecting each letter 
#from a different key in a dictionary.)
import itertools
d = {'1': ['a', 'b'], '2': ['c', 'd']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))'''
'''#Task 22 (Write a Python program to find the highest 3 values of corresponding keys in a dictionary.)
from heapq import nlargest
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)'''
''''#Task 25 (Write a Python program to print a dictionary in table format.)
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)'''
'''#Task 26 (Write a Python program to count the values associated with a key in a dictionary.)
student = [{'id': 1, 'success': True, 'name': 'Maciej'},
{'id': 2, 'success': False, 'name': 'Grzegorz'},
{'id': 3, 'success': True, 'name': 'Wojciech'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))'''
'''#Task 31 (Write a Python program to get the key, value and item in a dictionary.)
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key, '   ', value, '    ', count)'''
'''#Task 32 (Write a Python program to print a dictionary line by line.)
students = {'Maciej': {'class': 'A', 'roll_id': 2}, 'Grzegorz': {'class': 'B', 'roll_id': 3}}
for a in students:
    print(a)
    for b in students[a]:
        print(b, ':', students[a][b])'''
'''#Task 33 (Write a Python program to check if multiple keys exist in a dictionary.)
student = {
  'name': 'Maciej',
  'class': 'A',
  'roll_id': '2'
  }
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Maciej'})
print(student.keys() >= {'roll_id', 'name'})'''
'''#Task 34 (Write a Python program to count the number of items in a dictionary value that is a list.)
dict =  {'Maciej': ['subj1', 'subj2', 'subj3'], 'Szymon': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)'''
#Task 38 (Write a Python program to match key values in two dictionaries.)
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))


