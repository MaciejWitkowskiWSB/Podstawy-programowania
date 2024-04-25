'''#Task 1 (Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).)
nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
        print(','.join(nl))'''
'''#Task 3 (Write a  Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the
#guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.)
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')'''
'''#Task 4 (Write a Python program to construct the following pattern, using a nested for loop.)
n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')
for i in range(n, 0, -1):
            for j in range(i):
                print('* ', end="")
            print('')'''
'''#Task 5 (Write a Python program that accepts a word from the user and reverses it.)
word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")'''
'''#Task 6 (Write a Python program to count the number of even and odd numbers in a series of numbers)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
        print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)'''
'''#Task 7 (Write a Python program that prints each item and its corresponding type from the following list. 
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])
datalist = [1452, 11.23, 1+2j, True, 'task', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print("Type of", item, "is", type(item))'''
'''#Task 8 (Write a  Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.)
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
    print("\n")'''
'''#Task 9 (Write a  Python program to get the  Fibonacci series between 0 and 50. 
#Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
#Every next number is found by adding up the two numbers before it.)
x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y'''
'''#Task 12 (Write a  Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).)
lines = []
while True:
    l = input()
    if l:
         lines.append(l.upper())
    else:
        break;
    for l in lines:
        print(l)'''
'''#Task 14 (Write a Python program that accepts a string and calculates the number of digits and letters.)
s = input("Input a string")
d = l = 0
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print("Letters", l)
print("Digits", d)'''
'''#Task 16 (Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
#The numbers obtained should be printed in a comma-separated sequence.)
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))'''
'''#Task 17 (Write a Python program to print the alphabet pattern 'A'.)
def print_A(n):
    for i in range(n):
        for j in range((n // 2) + 1):
            if ((j == 0 or j == n // 2) and i != 0 or
                i == 0 and j != 0 and j != n // 2 or
                i == n // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()
height = 7
print_A(height)'''
'''#Task 27 (Write a Python program to print the alphabet pattern 'T'.)
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 3 or (row == 0 and column > 0 and column <6)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);'''
'''#Task 31 (Write a Python program to calculate a dog's age in dog years. Note: For the first two years, a dog year is equal to 10.5 human years. 
#After that, each dog year equals 4 human years.)
h_age = int(input("Input a dog's age in human years: "))
if h_age < 0:
    print("Age must be a positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2) * 4
print("The dog's age in dog's years is", d_age)'''
'''#Task 32 (Write a Python program to check whether an alphabet is a vowel or consonant.)
l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
else:
    print("%s is a consonant." % l)'''
'''#Task 34 (Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.)
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum 
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))'''
'''#Task 36 (Write a  Python program to check if a triangle is equilateral, isosceles or scalene. Note :An equilateral triangle is a 
#triangle in which all three sides are equal.A scalene triangle is a triangle that has three unequal sides.An isosceles triangle 
#is a triangle with (at least) two equal sides.)
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or z == x:
    print("Isosceles triangle")
else:
    print("Scalene triangle")'''
'''#Task 42 (Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.)
print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0
sum = 0.0
number = 1
while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1
if count == 0:
    print("Input some numbers")
else:
    print("Average and Sum of the above numbers are: ", sum / (count-1), sum)'''
'''#Task 43 (Write a Python program to create the multiplication table (from 1 to 10) of a number.)
n = int(input("Input a number: "))
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)'''
#Task 44 (Write a Python program to construct the following pattern, using a nested loop number.)
for i in range(10):
    print(str(i) * i)