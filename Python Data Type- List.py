'''#Task 1 (Write a Python program to sum all the items in a list.)
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([5, 7, -3]))'''
'''#Task 2 (Write a Python program to multiply all the items in a list.)
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
        return tot
print(multiply_list([5, 7, -3]))'''
'''#Task 3 (Write a Python program to get the largest number from a list.)
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
            return max
print(max_num_in_list([5, 7, -3]))'''
'''#Task 4 (Write a Python program to get the smallest number from a list.)
def min_num_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
            return min
print(min_num_list([5, 7, -3]))'''
'''#Task 6 (Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.)
def last(n):
    return n[-1]
def sort_list_last(tuples):
    return sorted(tuples, key = last)
print(sort_list_last([(2, 5), (1, 2), (4 ,4), (2, 3), (2, 1)]))'''
'''#Task 8 (Write a Python program to check if a list is empty or not.)
l = []
if not l:
    print("List is empty")'''
'''#Task 9 (Write a Python program to clone or copy a list.)
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)'''
'''#Task 14 (Write a Python program to print the numbers of a specified list after removing even numbers from it.)
num = [7, 8, 120, 25, 44, 20, 27]
num = [x for x in num if x % 2 != 0 ]
print(num)'''
'''#Task 15 (Write a Python program to shuffle and print a specified list.)
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)'''
'''#Task 19 (Write a Python program to calculate the difference between the two lists.)
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)'''
'''#Task 20 (Write a Python program to access the index of a list.)
nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)'''
'''#Task 21 (Write a Python program to convert a list of characters into a string.)
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)'''
'''#Task 22 (Write a Python program to find the index of an item in a specified list.)
num = [10, 30, 4, -6]
print(num.index(4))'''
'''#Task 23 (Write a Python program to find the index of an item in a specified list.)
import itertools
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
new_marget_list = list(itertools.chain(*original_list))
print(new_marget_list)'''
'''#Task 24 (Write a Python program to append a list to the second list.)
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)'''
'''#Task 25 (Write a Python program to select an item randomly from a list.)
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))'''
'''#Task 29 (Write a Python program to get unique values from a list.)
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ", my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : " , my_new_list)'''
'''#Task 35 (Write a Python program to create a list by concatenating a given list with a range from 1 to n.)
my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)'''
'''#Task 36 (Write a Python program to get a variable with an identification number or string.)
x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x'))'''
#Task 37 (Write a Python program to find common items in two lists.)
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))
    